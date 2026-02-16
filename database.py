from pymongo import MongoClient

# Database Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "blood_donation_db"

def get_db():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def init_db(db):
    """Seed database with initial data if empty."""
    if db is None:
        return

    # Seed Camps
    if db.camps.count_documents({}) == 0:
        camps_data = [
            {
                "title": "Vizag Community Blood Drive",
                "date": "April 15, 2026",
                "time": "9:00 AM - 4:00 PM",
                "location": "Vizag Community Center",
                "address": "Beach Road, Vizag, Andhra Pradesh",
                "slots": 45,
            },
            {
                "title": "Andhra University Donation Day",
                "date": "April 22, 2026",
                "time": "10:00 AM - 3:00 PM",
                "location": "Andhra University Campus",
                "address": "Kakinda Road, Vizag, Andhra Pradesh",
                "slots": 30,
            }
        ]
        db.camps.insert_many(camps_data)
        print("Initialized Camps Data")

    # Seed Testimonials
    if db.testimonials.count_documents({}) == 0:
        testimonials_data = [
            {
                "name": "Rajesh Kumar",
                "role": "Regular Donor",
                "quote": "I've been donating blood for over 5 years now. Simple way to make a difference.",
                "image": "images/testimonial1.jpg"
            },
            {
                "name": "Saritha Reddy",
                "role": "Blood Recipient",
                "quote": "Forever grateful to the donors who saved my life after my accident.",
                "image": "images/testimonial2.jpg"
            }
        ]
        db.testimonials.insert_many(testimonials_data)
        print("Initialized Testimonials Data")

    # Seed Stories
    if db.stories.count_documents({}) == 0:
        stories_data = [
            {
                "title": "A Second Chance at Life",
                "author": "Ravi Kumar",
                "type": "Recipient",
                "content": "Thanks to generous donors, I'm alive today."
            },
            {
                "title": "Why I Donate",
                "author": "Priya Rao",
                "type": "Donor",
                "content": "I helping someone's loved one."
            }
        ]
        db.stories.insert_many(stories_data)
        print("Initialized Stories Data")

