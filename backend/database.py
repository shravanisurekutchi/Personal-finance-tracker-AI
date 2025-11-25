from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1️⃣ Database URL
# Change password if yours is different
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/finance_db"

# 2️⃣ Create engine (echo=True prints SQL to terminal - helpful for debugging)
engine = create_engine(DATABASE_URL, echo=True)

# 3️⃣ Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4️⃣ Base model class
Base = declarative_base()

# 5️⃣ Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
