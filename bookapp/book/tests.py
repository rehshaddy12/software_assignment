from django.test import TestCase
from .models import Book
from django.urls import reverse

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date="2025-01-01"
        )

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.published_date.isoformat(), "2025-01-01")


class BookListViewTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Book 1", author="Author 1", published_date="2025-01-01")
        Book.objects.create(title="Book 2", author="Author 2", published_date="2025-01-02")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book 1")
        self.assertContains(response, "Book 2")
        self.assertTemplateUsed(response, 'books/book_list.html')
