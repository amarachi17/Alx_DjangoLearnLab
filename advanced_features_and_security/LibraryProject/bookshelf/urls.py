from django.urls import path
from .views import book_list, create_book, edit_book, delete_book

urlpatterns = [
    path("books/", book_list, name="book_list"),
    path("books/new/", create_book, name="book_create"),
    path("books/<int:book_id>/edit/", edit_book, name="book_edit"),
    path("books/<int:book_id>/delete/", delete_book, name="book_delete"),
]
