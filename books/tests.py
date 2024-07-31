from django.test import TestCase
from ninja.testing import TestClient
from django.urls import reverse
import json

from .models import Book
from .api import router
from .schemas import BookSchema, CreateBookSchema


class BookAPITest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="Test Book",
            author="Mickel",
            published_date="2024-07-28",
            isbn="1234567890111",
        )

        cls.client = TestClient(router)
        cls.headers = {
            'Content-Type': 'application/json'
        }

        return super().setUpTestData()

    def test_model_content(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Mickel")
        self.assertEqual(self.book.published_date, "2024-07-28")
        self.assertEqual(self.book.isbn, "1234567890111")

    def test_api_listview(self):
        response = self.client.get(reverse('api-1:list_books'))
        self.assertEqual(response.json(), [{
            "id": 1,
            "title": "Test Book",
            "author": "Mickel",
            "published_date": "2024-07-28",
            "isbn": "1234567890111"
            }]
        )

    def test_api_detailview(self):
        url = reverse('api-1:detail_book', kwargs={"book_id": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": "Test Book",
                "author": "Mickel",
                "published_date": "2024-07-28",
                "isbn": "1234567890111"
            }
        )

    # def test_api_updateview(self):
    #     url = reverse("api-1:update_book", kwargs={"book_id": self.book.id})
    #     response = self.client.put(url,
    #         {
    #             "title": "Name Change",
    #             "author": "Bob",
    #             "published_date": "2024-07-28",
    #             "isbn": "1234567890111"
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.json(),
    #         {
    #             "id": 1,
    #             "title": "Name Change",
    #             "author": "Bob",
    #             "published_date": "2024-07-28",
    #             "isbn": "1234567890111"
    #         }
    #     )
    #     self.assertEqual(self.book.title, "Name Change")
    #     self.assertEqual(self.book.author, "Bob")

    # def test_api_createview(self):
    #     url = reverse("api-1:create_book")
    #     response = self.client.post(
    #         url,
    #         json=json.dumps({
    #         "title": "New Book",
    #         "author": "New Author",
    #         "published_date": "2024-01-01",
    #         "isbn": "9876543210987"
    #     }))
    #     print(response.content)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Book.objects.count(), 2)
    #     self.assertEqual(response.json()["title"], "New Book")

    # def test_api_deleteview(self):
    #     url = reverse("api-1:delete_book", args=[self.book.id])
    #     response = self.client.delete(url)
    #     print(response.content)
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse(Book.objects.filter(id=1).exists())
