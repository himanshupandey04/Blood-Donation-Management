
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from database import get_db, init_db
from bson.objectid import ObjectId
from admin.routes import admin_bp
import os

app = Flask(__name__)
app.secret_key = 'blooddonation123'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.register_blueprint(admin_bp)

# Initialize Database
db = get_db()
init_db(db)

# ... (rest of imports/init) ...

# --- Context Processor ---
@app.context_processor
def inject_global_vars():
    user = get_session_user()
    return dict(
        user=user,
        user_name=user['name'] if user else None,
        current_year=datetime.now().year,
        is_admin=session.get('is_admin', False)
    )

def get_session_user():
    if 'user_id' not in session or db is None: return None
    try: return db.users.find_one({"_id": ObjectId(session['user_id'])})
    except: return None

@app.route('/')
def landing():
    if 'user_id' in session: return redirect(url_for('dashboard'))
    return redirect(url_for('auth'))

@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('auth'))
    
    camps = list(db.camps.find()) if db is not None else []
    testimonials = list(db.testimonials.find()) if db is not None else []

    return render_template('index.html', upcoming_camps=camps, testimonials=testimonials)





@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user = get_session_user()
    if not user: return redirect(url_for('auth'))

    if request.method == 'POST':
        updates = {
            "name": request.form['name'],
            "phone": request.form.get('phone'),
            "blood_group": request.form.get('blood_group'),
            "dob": request.form.get('dob'),
            "address": request.form.get('address')
        }

        # Handle Image Upload
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                # Ensure unique filename to prevent cache issues
                unique_filename = f"{user['_id']}_{int(datetime.now().timestamp())}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                updates['profile_image'] = unique_filename

        db.users.update_one({"_id": user['_id']}, {"$set": updates})
        flash("Profile updated successfully!", "success")
        return redirect(url_for('profile'))

    return render_template('profile.html')
    
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('auth'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if db is None:
        flash("Database Error!", "danger")
        return redirect('/auth')

    user = db.users.find_one({"email": email})

    if user and check_password_hash(user['password_hash'], password):
        session['user_id'] = str(user['_id'])
        session['is_admin'] = (user['email'] == 'admin@bloodlife.com')
        target = url_for('admin.dashboard') if session['is_admin'] else url_for('dashboard')
        return redirect(target)
    else:
        flash("Invalid credentials", "danger")
        return redirect('/auth')

@app.route('/signup', methods=['POST'])
def signup():
    if db is None: return redirect('/auth')
    
    if db.users.find_one({"email": request.form['email']}):
        flash("Email already registered.", "danger")
    else:
        db.users.insert_one({
            "name": request.form['name'],
            "email": request.form['email'],
            "password_hash": generate_password_hash(request.form['password']),
            "created_at": datetime.now()
        })
        flash('Account created! Please login.', 'success')

    return redirect(url_for('auth'))

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        if db is not None:
            result = db.donations.insert_one({
                "donor_name": request.form['name'],
                "donor_email": request.form['email'],
                "donor_phone": request.form['phone'],
                "donor_age": request.form['age'],
                "donor_blood_group": request.form['bloodGroup'],
                "last_donation": request.form.get('lastDonation'),
                "medical_conditions": request.form.get('medicalConditions'),
                "available": 'available' in request.form,
                "address": request.form['address'],
                "submitted_at": datetime.now()
            })
            flash("Registered successfully!", "success")
            return redirect(url_for('confirmation', type='donation', id=str(result.inserted_id)))
        return redirect(url_for('donate'))

    return render_template('donate.html')

@app.route('/submit_request', methods=['POST'])
def submit_request():
    if db is not None:
        result = db.patient_requests.insert_one({
            "patient_name": request.form.get('patientName'),
            "patient_age": request.form.get('patientAge'),
            "blood_group_needed": request.form.get('bloodGroupNeeded'),
            "hospital": request.form.get('hospital'),
            "reason": request.form.get('reason'),
            "urgency": request.form.get('urgency'),
            "is_emergency": 'isEmergency' in request.form,
            "units_required": request.form.get('unitsRequired'),
            "contact_name": request.form.get('contactName'),
            "contact_phone": request.form.get('contactPhone'),
            "contact_email": request.form.get('contactEmail'),
            "submitted_at": datetime.now()
        })
        flash("Request submitted!", "success")
        return redirect(url_for('confirmation', type='request', id=str(result.inserted_id)))
    return redirect(url_for('donate'))

@app.route('/confirmation/<type>/<id>')
def confirmation(type, id):
    if type == 'donation':
        data = db.donations.find_one({"_id": ObjectId(id)})
    else:
        data = db.patient_requests.find_one({"_id": ObjectId(id)})
        
    if not data:
        flash("Record not found.", "danger")
        return redirect(url_for('dashboard'))
        
    return render_template('slip.html', data=data, type=type)

@app.route('/stories')
def stories_page():
    stories = list(db.stories.find()) if db is not None else []
    return render_template('stories.html', stories=stories)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    # Simple static content
    faq_data = [
        {"title": "General", "questions": [{"q": "Who can donate?", "a": "Healthy adults 17+."}]}
    ]
    return render_template('faq.html', faq_categories=faq_data)

@app.route('/api/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '').lower()
    resp = "I didn't understand that."
    
    if 'hello' in msg: resp = "Hello! Ask me about blood donation."
    elif 'donate' in msg: resp = "You must be 17+ to donate."
    elif 'emergency' in msg: resp = "Call 108 for emergencies."
    
    return jsonify({'response': resp})

if __name__ == '__main__':
    app.jinja_env.globals.update(enumerate=enumerate)
    app.run(debug=True, port=5001, host='localhost')
