# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 🔧 SWITCH DATABASE HERE:

# ✅ Option A: MySQL (RECOMMENDED for production)
# Example: mysql+pymysql://user:password@localhost:3306/gita_db
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/gita_db")

# ✅ Option B: SQLite (only use for testing)
DATABASE_URL = "sqlite:///./gita.db"

# ⚠️ Use connect_args ONLY for SQLite
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

# 🔧 Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔧 Base class for all ORM models
Base = declarative_base()


# ✅ Utility function to initialize DB (called from main.py)
def create_db():
    from app.models import user_model, verse_model  # ⬅️ Add all your models here
    Base.metadata.create_all(bind=engine)
