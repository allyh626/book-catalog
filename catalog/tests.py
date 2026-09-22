from django.test import TestCase

from django.test import TestCase
from .models import Publisher, Book


class BookPageTest(TestCase):

    def test_book_appears_on_books_page(self):
        publisher = Publisher.objects.create(name="Test Publisher")
        Book.objects.create(
            title="Unique Test Book 8472",
            in_print=True,
            publisher=publisher
        )

        response = self.client.get("/")

        self.assertContains(response, "Unique Test Book 8472")
