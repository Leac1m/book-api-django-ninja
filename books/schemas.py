from ninja import Schema
from datetime import date
from ninja import FilterSchema
from typing import Optional, List

from reviews.schemas import ReviewSchema

class BookSchema(Schema):
    id: int
    title: str
    author: str
    published_date: date
    isbn: str


class CreateBookSchema(Schema):
    title: str
    author: str
    published_date: date
    isbn: str

class BookFilterSchema(FilterSchema):
    title: Optional[str] = None
    author: Optional[str] = None
    published_date: Optional[date] = None
    isbn: Optional[str] = None

class BookReviewSchema(Schema):
    title: str
    author: str
    published_date: date
    isbn: str
    reviews: List[ReviewSchema] = None