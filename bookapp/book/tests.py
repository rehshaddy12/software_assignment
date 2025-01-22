from django.test import TestCase
from .models import Book,BookManagement,User
from django.urls import reverse
import unittest

class BookModelTest(unittest.TestCase):     #I ADDED unittest
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date="2025-01-01"
        )

     #my addition start here @elikana   
        self.manager = BookManagement()

    def test_sign_up_valid(self):
        """Test if a user can sign up successfully with valid details."""
        user = self.manager.sign_up("valid_username", "valid_password")
        self.assertEqual(user.username, "valid_username")
        self.assertEqual(user.password, "valid_password")
        self.assertIn("valid_username", self.manager.users)

    def test_sign_up_existing_user(self):
        """Test if an error is raised when signing up with an existing username."""
        self.manager.sign_up("duplicate_user", "password123")
        with self.assertRaises(ValueError):
            self.manager.sign_up("duplicate_user", "another_password")

    def test_sign_up_invalid(self):
        """Test if an error is raised when signing up with invalid details."""
        with self.assertRaises(ValueError):
            self.manager.sign_up("", "password")  # Empty username
        with self.assertRaises(ValueError):
            self.manager.sign_up("username", "")  # Empty password

if __name__ == "__main__":
    unittest.main()
#my addition end here @elikana

    
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


