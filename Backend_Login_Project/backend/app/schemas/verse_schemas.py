# app/schemas/verse.py

from pydantic import BaseModel

class VerseBase(BaseModel):
    chapter: int
    verse: int
    text: str
    translation: str

class VerseOut(VerseBase):
    id: int

    class Config:
        orm_mode = True
