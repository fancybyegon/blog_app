# 📝 Flask Blog API

This is a RESTful API for a simple blogging platform built with **Flask**, **SQLAlchemy**, and **Flask-Migrate**. It allows users to create accounts, write blog posts, and leave comments. This project was built for a code challenge and follows clean architecture, REST conventions, and includes validation, proper response structure, and JSON output.

---

## 📚 Features

- Create Users
- Create, Read, Update, Delete (CRUD) for Posts
- Comment on Posts
- JSON responses with nested relationships
- Validation for required fields
- Returns correct HTTP status codes

---

## 🏗️ Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite (for development)
- Postman (for testing)

---

## 📁 Project Structure

blog_app/
├── app/
│ ├── init.py
│ ├── models.py
│ └── routes.py
├── migrations/
├── run.py
├── config.py
├── .flaskenv
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <https://github.com/fancybyegon/blog_app>
cd blog_app


python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt


flask db init
flask db migrate -m "Initial migration"
flask db upgrade


flask run
