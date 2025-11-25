from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from models import Expense
from routes.expenses import router as expenses_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,
    allow_methods=["*"],            
    allow_headers=["*"],            
)

print("Creating tables if they do not exist...")
Base.metadata.create_all(bind=engine)

app.include_router(expenses_router)


@app.get("/")
def home():
    return {"message": "Personal Finance Tracker Backend is running!"}
