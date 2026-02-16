from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_db
from bson.objectid import ObjectId
from datetime import datetime

# Create a Blueprint for admin routes
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def is_admin():
    """Check if the current user is an admin."""
    return session.get('is_admin', False)

@admin_bp.route('/')
def dashboard():
    if not is_admin():
        flash("Access Denied: Admins only.", "danger")
        return redirect(url_for('auth'))

    db = get_db()
    if db is None:
        return "Database Error", 500

    # Fetch data for the dashboard
    donations = list(db.donations.find().sort("submitted_at", -1))
    requests = list(db.patient_requests.find().sort("submitted_at", -1))
    camps = list(db.camps.find().sort("date", 1))
    testimonials = list(db.testimonials.find())

    return render_template('admin/dashboard.html', 
                         donations=donations, 
                         requests=requests,
                         camps=camps,
                         testimonials=testimonials)

# --- Content Management Routes ---

@admin_bp.route('/add_camp', methods=['POST'])
def add_camp():
    if not is_admin(): return redirect(url_for('auth'))
    
    db = get_db()
    
    new_camp = {
        "title": request.form['title'],
        "date": request.form['date'],
        "time": request.form['time'],
        "location": request.form['location'],
        "slots": request.form['slots']
    }
    
    db.camps.insert_one(new_camp)
    flash("Camp added successfully!", "success")
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete_camp/<camp_id>')
def delete_camp(camp_id):
    if not is_admin(): return redirect(url_for('auth'))
    
    db = get_db()
    db.camps.delete_one({"_id": ObjectId(camp_id)})
    flash("Camp deleted.", "success")
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/add_testimonial', methods=['POST'])
def add_testimonial():
    if not is_admin(): return redirect(url_for('auth'))
    
    db = get_db()
    
    new_testimonial = {
        "name": request.form['name'],
        "role": request.form['role'], # e.g., Donor, Recipient
        "quote": request.form['quote']
    }
    
    db.testimonials.insert_one(new_testimonial)
    flash("Testimonial added!", "success")
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete_testimonial/<t_id>')
def delete_testimonial(t_id):
    if not is_admin(): return redirect(url_for('auth'))
    
    db = get_db()
    db.testimonials.delete_one({"_id": ObjectId(t_id)})
    flash("Testimonial deleted.", "success")
    return redirect(url_for('admin.dashboard'))
