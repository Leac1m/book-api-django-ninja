from django.db import models
from books.models import Book
from accounts.models import CustomUser

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.review[0:50]