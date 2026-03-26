<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=180&section=header&text=Blood%20Donation%20Management&fontSize=40&fontAlignY=40&desc=Flask%20%2B%20MongoDB%20Donor%20%26%20Request%20Management%20System&descAlignY=62&descSize=16&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.x-47A248?style=flat&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)]()

</div>

---

## Overview

A full-stack web application for blood banks and healthcare organizations to digitize donor management, patient requests, and donation camp scheduling. Built to replace phone-call and paper-ledger workflows with a centralized, real-time system.

**The problem it solves:** Blood banks in India often have no live view of donor availability. When a patient urgently needs blood, staff make phone calls to a ledger list — slow, error-prone, and often outdated. This system centralizes everything.

---

## Features

### 👤 Donor Portal
- Donor registration with blood group, availability, and contact info
- Login / Signup with bcrypt password hashing
- View upcoming donation camps
- Testimonials board

### 🏥 Admin Dashboard
- Full table of all registered donors, filterable by blood group
- Incoming urgent patient requests with status tracking
- Camp management: create and list upcoming events

### 🤖 Chatbot Assistant
- Interactive FAQ bot for common queries (donation eligibility, process, camp dates)

### 🩺 Patient Request System
- Public form for urgent blood requests
- Requests queued to admin dashboard for action

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask 2 |
| Database | MongoDB (via PyMongo) |
| Frontend | Jinja2 templates, Bootstrap 5, custom CSS |
| Auth | bcrypt password hashing |
| Deployment | Local (Flask dev server) |

---

## Project Structure

```
blood_donation_website/
├── app.py                  # Main Flask application
├── database.py             # MongoDB connection & data seeding
├── requirements.txt        # Python dependencies
├── static/                 # CSS, JS, images
└── templates/              # Jinja2 HTML templates
    ├── index.html          # Home / landing
    ├── donor_form.html     # Donor registration
    ├── admin.html          # Admin dashboard
    └── ...
```

---

## Getting Started

### Prerequisites
- Python 3.x
- MongoDB Community Server running on port `27017`

### Installation

```bash
git clone https://github.com/himanshupandey04/Blood-Donation-Management.git
cd Blood-Donation-Management
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Access at **http://localhost:5001**

### Admin Access

| Field | Value |
|---|---|
| Sign up email | `admin@bloodlife.com` |
| Admin panel | `/admin` |

---

## Contributing

Issues and pull requests are welcome. See the main profile for contribution guidelines.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

<div align="center">
<br/>
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=80&section=footer" width="100%"/>
</div>
