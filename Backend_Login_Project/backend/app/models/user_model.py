# app/models/user.py

from sqlalchemy import Column, Integer, String
# from bhagavadgita_project.backend.app.core.database_core import Base
from app.core.database_core import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # ✅ YOU CAN CUSTOMIZE: add fields like email, full_name later
