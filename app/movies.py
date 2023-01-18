from pydantic import BaseModel
from datetime import date

class Movie(BaseModel):
    title: str
    studio: str
    duration: str
    date: date
    summary: str
    genres: str = None
