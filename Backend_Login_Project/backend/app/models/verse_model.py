# app/models/verse.py

from sqlalchemy import Column, Integer, String
from app.core.database_core import Base

class Verse(Base):
    __tablename__ = "verses"
    id = Column(Integer, primary_key=True, index=True)
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String)
    translation = Column(String)

    # ✅ YOU CAN CUSTOMIZE: Add "section", "speaker", "tags" later
