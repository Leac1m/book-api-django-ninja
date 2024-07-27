from django.shortcuts import get_object_or_404 
from ninja import NinjaAPI

from .models import Book
from .schemas import BookSchema, CreateBookSchema


api = NinjaAPI()

@api.get('/books', response=list[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books


@api.post('/books', response=BookSchema)
def create_book(request, payload: CreateBookSchema):
    book = Book.objects.create(**payload.dict())
    return book


@api.get('/books/{book_id}', response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@api.put('books/{book_id}', response=BookSchema)
def update_book(request, book_id: int, payload: CreateBookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(Book, attr, value)
    book.save()
    return book


@api.delect('books/{book_id}')
def delect_book(request, book_id: int)
    book = get_object_or_404(Book, id=book_id)
    book.delect()
    return {'success': True}

