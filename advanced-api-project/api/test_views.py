from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Set up the test data before running each test case.
        self.author = Author.objects.create(name="J.k. Rowlings Abel")
        self.book = Book.objects.create(
            title = "Harry Potter",
            author = self.author,
            publication_year = 1998
        )
        self.list_url = reverse("book-list") # Use the name defined in urls.py
        self.detail_url = reverse("book-detail", args=[self.book.id])

        def test_create_book(self):
            # Testing the Create function
            data = {
                'title': 'The Hobbit',
                'author': self.author.id,
                'publication_year': 1987
            }
            response = self.cilent.post(self.list_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Book.objects.count(), 2)

        def test_list_books(self):
            # Test retrieving all books.
            response = self.client.get(self.detail_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1) # Ensures only 1 book exists

        def test_retrieve_book_detail(self):
            # Test to retrieve one book by ID.
            response = self.client.get(self.detail_url)
            self.assertEqual(response.status_code,status.HTTP_200_OK)
            self.assertEqual(response.data['title'], self.book.title)

        def test_update_book(self):
            # Test to update a book.
            data = {"title": "Harry Potter and the Sorcerer's Stone"}
            response = self.client.patch(self.detail_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.book.refresh_from_db()
            self.assertEqual(self.book.title, data['title'])

        def test_delete_bool(self):
            # Test to delete a book.
            response = self.client.delete(self.detail_url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Book.objects.count(), 0)

class AuthenticatedBookAPITestCase(APITestCase):
    def setUp(self):
        # Set up authenticated user for testing.
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)

    def test_authenticated_user_can_create_book(self):
        # Ensures only authenticated users can create books.
        data = {'title': 'Django Book', 'author': 1, 'publication_year':2018}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
