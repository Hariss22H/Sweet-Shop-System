# 🍬 Sweet Shop Management System

A full-stack Sweet Shop Management System built using FastAPI and React.
The application allows users to register, log in, view sweets, purchase items,
and manage inventory with admin controls.

---

## 🚀 Features

### Backend (FastAPI)
- User registration and login (JWT authentication)
- Password hashing using bcrypt
- Sweet CRUD operations
- Search sweets by name and category
- Inventory management:
  - Purchase sweets (stock decreases)
  - Restock sweets (admin only)
- SQLite database (persistent storage)
- Swagger API documentation
- Test-Driven Development (TDD) for authentication

### Frontend (React + Vite)
- User registration and login UI
- Sweet dashboard with live inventory
- Purchase button disabled when stock is zero
- Axios-based API integration
- Simple, clean, responsive UI

---

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- pytest

**Frontend**
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
```


## Backend runs at:

http://127.0.0.1:8000

---

### Swagger UI:

http://127.0.0.1:8000/docs

Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

http://localhost:5173
---
🧪 Running Tests
```bash

cd backend
pytest
```

🤖 My AI Usage
---

I used AI tools (ChatGPT) responsibly throughout this project for:

Understanding project requirements

Designing API endpoint structure

Writing initial boilerplate code

Debugging issues (bcrypt compatibility, CORS errors)

Improving code readability and structure

All AI-assisted code was reviewed, modified, and fully understood by me.
AI significantly improved my productivity while allowing me to focus on learning
best practices such as TDD, clean architecture, and proper Git usage.
---
📌 Notes
---
Authentication is implemented using JWT.

Inventory logic ensures stock validation.

The project follows clean coding practices and modular structure.
---

## 👨‍💻 Author
**SHAIK HARRISS RAZVI**  
🔗 [LinkedIn](https://www.linkedin.com/in/hariss-razvi-shaik-31b037333/) | [GitHub](https://github.com/Hariss22H)
