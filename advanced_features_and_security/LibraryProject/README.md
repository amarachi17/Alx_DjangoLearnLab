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


# Django Security Best Practices

## 1. Configured Security Settings
- `DEBUG = False`: Disabled debugging in production.
- `CSRF_COOKIE_SECURE = True`: CSRF tokens only work over HTTPS.
- `SESSION_COOKIE_SECURE = True`: Prevents session hijacking.
- `SECURE_BROWSER_XSS_FILTER = True`: Protects against XSS.
- `CSP`: Restricts allowed content sources.

## 2. Secure Coding Practices
- All forms include `{% csrf_token %}` for CSRF protection.
- Django ORM prevents SQL injection.
- Input validation is implemented to sanitize user data.

## 3. Security Testing
- Manually tested CSRF protention using the browser's developer tools.
- Attemptes XSS injection to verify CSP headers are working.

# Security Configurations

## HTTPS Enforcement
- All HTTP requests are redirected to HTTPS.
- HSTS is enabled for 1 year with subdomain support and preloading.

## Secure Cookies
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE are set to `True` to prevent transmission over HTTP.

## Secure Headers
- X-Frame-Options set `DENY` (protects against clickjacking).
- SECURE_CONTENT_TYPE_NOSNIFF enabled (prevents MIME-type sniffing).
- SECURE_BROWSER_XSS_FILTER enabled (protects against XSS attacks).

