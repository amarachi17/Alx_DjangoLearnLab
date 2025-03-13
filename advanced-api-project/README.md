# Advanced API Project

This project demostrates how to create custom views and generic views using Djang REST Framework to manage CRUD operations on a Book model.

## Endpoints

- **GET /api/books/**
    List all books ( No authentication required).

- **GET /api/books/<id>**
    Retrieve details for a specific book.

- **POST /api/books/create/**
    Create a new book (Authentication required).

- **PUT/PATCH /api/books/<id>/update/**
    Update an existing book (Authentication required).

- **DELETE /api/books/<id>/delete/**
    Delete an existing book (Authentication required).