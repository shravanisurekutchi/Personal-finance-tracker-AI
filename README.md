#Personal Finance Tracker (AI-Powered)
### FastAPI • React • PostgreSQL • SQLAlchemy • Recharts

A full-stack **AI-powered personal finance tracker** that helps users log expenses, visualize spending patterns, and get smart insights.  
Built using **FastAPI (Python)** for backend, **React** for frontend, **PostgreSQL** for storage, and simple AI-logic for auto-categorization.

---

## Features

### **AI-Driven Categorization**
- Automatically assigns category (food, bills, transport, shopping, entertainment, etc.)
- Based on keyword inference from the expense title
- No external API required

### **Expense Management**
- Add expenses with title + amount  
- View all expenses in a sortable table  
- PostgreSQL persistence with SQLAlchemy ORM  

### **Analytics Dashboard**
- Pie chart of spending by category  
- Bar chart of total amount per category  
- Trends update as soon as new expenses are added  

### **Smart Insights (AI-Like Behaviour)**
- Total spent  
- Highest spending category  
- Average per transaction  
- Personalized suggestions such as:  
  _“You are spending a lot on food — consider cooking at home.”_

---

## Tech Stack

**Frontend**
- React (create-react-app)
- Axios (API calls)
- Recharts (charts & visualization)

**Backend**
- FastAPI
- SQLAlchemy ORM
- PostgreSQL  
- Pydantic Models

**Other**
- CORS middleware  
- JSON REST APIs  

---

## Project Structure

ai-finance-tracker/
│
├── backend/
│ ├── main.py
│ ├── models/
│ ├── routes/
│ ├── database.py
│ ├── venv/ (ignored)
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── ExpenseForm.js
│ │ │ ├── ExpensesList.js
│ │ │ ├── ExpensesChart.js
│ │ │ ├── InsightsCard.js
│ ├── node_modules/ (ignored)
│
└── .gitignore

---

## **Backend Setup (FastAPI)**

1️. Create virtual environment
python -m venv venv
venv\Scripts\activate
2️. Install dependencies
pip install fastapi uvicorn psycopg2 sqlalchemy pydantic
pip install "python-multipart"
3. Start backend
uvicorn main:app --reload
Backend runs at:
http://127.0.0.1:8000


## **Frontend Setup (React)

1. Install packages
npm install
2. Start React development server
npm start
Frontend runs at:
http://localhost:3000

