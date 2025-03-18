## This project is a Django based blog with a complete user authentication system, allowing users to register, login, logout and manage their profiles. It utilized Django's built in authentication framework while extending it with custom features.

Features:
- User registration with email verification
- Secure login and logout system
- Profile management with editable user details
- CSRF protection for security
- Passwrd hashing using Django's built in system

Security and Permissions
- CSRF Protection - Ensures secure form submission
- Authentication Requires - Users must log in to creatw posts
- Author Restrictions - Only the author can edit or delete theor posts
