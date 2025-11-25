from database import Base, engine
from models import Expense

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
