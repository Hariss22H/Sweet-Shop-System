# 🍬 Sweet Shop Management System

A full-stack Sweet Shop Management System built using **FastAPI** and **React**.  
This application allows users to register, log in, view available sweets, purchase items, and manage inventory through secure REST APIs.

---

## 🚀 Features

### Backend (FastAPI)
- User registration and login with **JWT authentication**
- Secure password hashing using **bcrypt**
- Sweet CRUD operations (Create, Read, Update, Delete)
- Search sweets by name and category
- Inventory management:
  - Purchase sweets (automatically decreases stock)
  - Prevents purchase when stock is zero
  - Restock sweets (admin-controlled logic)
- Persistent storage using **SQLite**
- Interactive API documentation using **Swagger UI**
- **Test-Driven Development (TDD)** followed for authentication module

---

### Frontend (React + Vite)
- User registration and login interface
- Sweet dashboard displaying live inventory
- Purchase button disabled when stock is unavailable
- API integration using **Axios**
- Simple, clean, and responsive user interface

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- pytest

### Frontend
- React
- Vite
- Axios
- JavaScript

---

## ⚙️ Setup Instructions

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at:
http://localhost:5173

🧪 Running Tests
cd backend
pytest

🤖 My AI Usage

I used AI tools (ChatGPT) responsibly throughout this project for:

Understanding project requirements and scope

Designing REST API structure and data models

Generating initial boilerplate code

Debugging issues (bcrypt compatibility, CORS configuration)

Improving code readability and structure

All AI-generated suggestions were reviewed, modified, and fully understood before implementation.
AI significantly improved my productivity while allowing me to focus on learning best practices such as Test-Driven Development (TDD), clean architecture, and proper Git workflows.

📌 Notes

Authentication is implemented using JWT

Inventory logic ensures stock validation and consistency

Virtual environments, dependencies, and database files are excluded using .gitignore

The project follows clean coding principles and modular structure