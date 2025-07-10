# app/api/verse.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database_core import SessionLocal
from app.crud import verse_crud as crud_verse
from app.schemas.verse_schemas import VerseOut
import json
from pathlib import Path

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=list[VerseOut])
def read_all_verses(db: Session = Depends(get_db)):
    return crud_verse.get_all_verses(db)

@router.get("/search", response_model=list[VerseOut])
def search(chapter: int = None, keyword: str = None, db: Session = Depends(get_db)):
    return crud_verse.search_verses(db, chapter=chapter, keyword=keyword)

@router.post("/load")
def load_data(db: Session = Depends(get_db)):
    # ✅ YOU CAN DISABLE: or password protect this route in production
    json_path = Path(__file__).resolve().parents[2] / "app" / "data" / "verses.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    crud_verse.load_verses_from_json(db, data)
    return {"message": f"{len(data)} verses loaded."}
