# app/crud/verse.py

from sqlalchemy.orm import Session
from app.models.verse_model import Verse
from app.schemas.verse_schemas import VerseBase

def load_verses_from_json(db: Session, json_data: list):
    for item in json_data:
        verse = Verse(**item)
        db.add(verse)
    db.commit()

def get_all_verses(db: Session):
    return db.query(Verse).all()

def search_verses(db: Session, chapter: int = None, keyword: str = None):
    query = db.query(Verse)
    if chapter:
        query = query.filter(Verse.chapter == chapter)
    if keyword:
        keyword = f"%{keyword.lower()}%"
        query = query.filter(Verse.text.ilike(keyword) | Verse.translation.ilike(keyword))
    return query.all()
