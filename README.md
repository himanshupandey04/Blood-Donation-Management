# Blood Donation Management System
![Status](https://img.shields.io/badge/Status-Active-success) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![MongoDB](https://img.shields.io/badge/MongoDB-Latest-green)

A professional, student-friendly web application for managing blood donations, patient requests, and upcoming donation camps. Built with **Flask** and **MongoDB**.

## 🚀 Features

*   **User Authentication**: Secure Login & Signup with password hashing.
*   **Donation Registration**: Easy form for donors to register availability.
*   **Patient Requests**: Urgent blood request submission system.
*   **Dashboard**:
    *   **User Dashboard**: View upcoming camps and testimonials.
    *   **Admin Dashboard**: View all registered donors and requests in a table format.
*   **Chatbot**: Interactive AI-powered (rule-based) assistant for FAQs.
*   **Responsive Design**: Professional UI using Bootstrap and custom CSS.
*   **Database**: robust **MongoDB** integration for storing all records.

## 📂 Project Structure

```
blood_donation_website/
│
├── app.py              # Main Application Entry Point
├── database.py         # Database Connection & Seeding Logic
├── requirements.txt    # Python Dependencies
├── README.md           # Documentation
│
├── static/             # CSS, JS, Images
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/          # HTML Templates (Jinja2)
    ├── auth.html       # Login/Signup Page
    ├── index.html      # Main Dashboard
    ├── donate.html     # Donation Forms
    ├── admin_dashboard.html # Admin View
    └── ...
```

## 🛠️ Prerequisites

1.  **Python 3.x** installed.
2.  **MongoDB** Community Server installed and running locally on port `27017`.
    *   [Download MongoDB](https://www.mongodb.com/try/download/community)

## ⚡ How to Run

1.  **Clone/Download** this folder.
2.  **Install Dependencies**:
    Open a terminal/command prompt in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Start MongoDB**: Ensure your MongoDB server is running.
4.  **Run the App**:
    ```bash
    python app.py
    ```
5.  **Access the App**:
    Open your browser and go to: **[http://localhost:5001](http://localhost:5001)**

## 🧪 Admin Credentials & Testing

*   **Test Account**: You can sign up with any email.
*   **Admin Access**:
    1.  Sign Up with email: `admin@bloodlife.com`
    2.  Login.
    3.  Go to `http://localhost:5001/admin` to see all data.

## 📝 For Students/Teachers

*   **Explanation**: This project uses **Flask** (a micro-web framework) for the backend and **MongoDB** (NoSQL database) for flexibility. 
*   **Logic**: The chatbot uses simple conditional logic (`if-else`) in Python to demonstrate basic AI concepts without complex libraries.
*   **Database**: The `init_db` function in `database.py` automatically checks if the database is empty and adds dummy data (Camps, Testimonials) so the app never looks empty during a presentation.

---
*Created for Educational Purpose.*
