# LibraryProject - Django Setup Guide

# Objective
Set up a Django development environment and create a basic Django project.

## Installation steps
1. Install Django:
   - Open your terminal or command prompt.
   - Run the following command to install Django:
     ```
     pip install django
     ```

2. Create a new Django project:
   - Run the following command in your terminal or command prompt to create a new Django project:
     ```
     django-admin startproject libraryproject
     ```
3. Navigate to the project directory:
     ```
     cd libraryproject
     ```

4. Run the Django development server:
     ```
     python manage.py runserver
     ```

Your Django development environment is now set up and you can start creating your first Django project.

## Project structure

# Permisions and Groups in Django

## Custom Permissions
- `can_view`: Allows users to view documents.
- `can_create`: Allows users to create documents.
- `can_edit`: Allows users to edit documents.
- `can_delete`: Allows users to delete documents.

## Groups and Assigned Permissions
- **Editors** - can_create, can_edit
- **Viewers** - can_view
- **Admins** - can_create, can_edit, can_delete

## Testing
- Log in as a user with different roles and verify permissions.

## How to Add a User to a Group
1. Open Django Admin
2. Navigate to **Users**.
3. Select a user and assign them to a group


