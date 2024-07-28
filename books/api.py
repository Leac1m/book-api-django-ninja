from django.shortcuts import get_object_or_404 
from ninja import NinjaAPI, Router

from .models import Book
from .schemas import BookSchema, CreateBookSchema


api = NinjaAPI(version=1)
router = Router()

@router.get('/books', response=list[BookSchema], url_name='list_books')
def list_books(request):
    books = Book.objects.all()
    return books


@router.post('/books', response=BookSchema, url_name='create_book')
def create_book(request, payload: CreateBookSchema):
    book = Book.objects.create(**payload.dict())
    return book


@router.get('/books/{book_id}', response=BookSchema, url_name='detail_book')
def detail_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@router.put('books/{book_id}', response=BookSchema, url_name='update_book')
def update_book(request, book_id: int, payload: CreateBookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(Book, attr, value)
    book.save()
    return book


@router.delete('books/{book_id}', url_name='delete_book')
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delect()
    return {'success': True}

api.add_router("", router)