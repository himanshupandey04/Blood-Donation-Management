# Blood Donation Management System

A software system for managing blood donations, patient requests, and upcoming donation camps. Built with Flask and MongoDB.

### Features

-   **User Authentication**: Login and Signup with password hashing.
-   **Donation Registration**: Form for donors to register availability.
-   **Patient Requests**: Urgent blood request submission system.
-   **Dashboard**:
    -   User Dashboard: View upcoming camps and testimonials.
    -   Admin Dashboard: View all registered donors and requests in a table format.
-   **Chatbot**: Interactive assistant for FAQs.
-   **Responsive Design**: Professional UI using Bootstrap and custom CSS.
-   **Database**: MongoDB integration for storing all records.

### Project Structure

```
blood_donation_website/
├── app.py              # Main Application Entry Point
├── database.py         # Database Connection & Seeding Logic
├── requirements.txt    # Python Dependencies
├── README.md           # Documentation
├── static/             # CSS, JS, Images
└── templates/          # HTML Templates
```

### Prerequisites

1.  Python 3.x
2.  MongoDB Community Server (27017)

### How to Run

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Start MongoDB**: Ensure server is running.
3.  **Run the App**:
    ```bash
    python app.py
    ```
4.  **Access the App**: [http://localhost:5001](http://localhost:5001)

### Admin Credentials

-   Sign Up with: `admin@bloodlife.com`
-   Access admin view at: `/admin`
