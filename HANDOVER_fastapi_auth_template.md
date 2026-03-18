# FastAPI Auth Template -- Handover Documentation

This document summarizes the current state of the project so development
can continue smoothly in a future session.

## Project Goal

Build a reusable authentication module for FastAPI that can be reused
across multiple APIs.

Key goals:

-   Understand JWT authentication
-   Build a reusable auth module
-   Keep architecture modular and scalable
-   Make it suitable for future FastAPI projects

## Current Implementation

The project currently supports:

-   User registration
-   User login
-   JWT token generation
-   Password hashing using Passlib + Argon2
-   Dependency-based route protection

Authentication flow:

1.  User registers with username, email, and password.
2.  Password is hashed before storing.
3.  User logs in with credentials.
4.  Server verifies password.
5.  JWT access token is issued.
6.  Protected routes validate the token.

## Current Architecture

Key components:

### Core

`core/config.py` - Environment configuration using pydantic-settings

`core/security.py` - Password hashing - Password verification - JWT
token creation

### Database

`db/database.py` - SQLAlchemy database setup

`db/models.py` - User model

### Schemas

`schemas/auth_schema.py` - Request/response models

### Services

`services/auth_service.py` - Registration logic - Authentication logic

### API

`api/auth_routes.py` - Register endpoint - Login endpoint

### Dependencies

`dependencies/auth_dependencies.py` - JWT validation dependency -
Protects routes

### Main Application

`main.py` - Initializes FastAPI - Registers routers - Creates database
tables

## Known Decisions

Argon2 was chosen instead of bcrypt because:

-   bcrypt has a 72 byte password limit
-   compatibility issues with Python 3.12
-   Argon2 is the modern recommended hashing algorithm

## Current Limitations

The system currently only supports:

-   Access tokens
-   Basic user authentication

Missing features:

-   Refresh tokens
-   Logout token invalidation
-   Role-based access control
-   Email verification
-   Password reset
-   Rate limiting
-   API key authentication

## Suggested Next Steps

Future improvements should include:

1.  Implement refresh tokens
2.  Token rotation strategy
3.  Role-based permissions
4.  Admin vs user authorization
5.  Token blacklist for logout
6.  Optional OAuth login

## Questions to Continue Development

When resuming the project, the next conversation should clarify:

-   Should refresh tokens be implemented?
-   Should roles (admin/user/trainer/student) be added?
-   Should this become a standalone auth service?
-   Should PostgreSQL replace SQLite?

## How to Resume Development

To continue the project:

1.  Load the project structure.
2.  Review README.md.
3.  Confirm dependencies.
4.  Decide next authentication feature to implement.


### 3/18/2026 — Authentication Improvements

**Changes Implemented**

* Updated authentication login route to use `OAuth2PasswordRequestForm` instead of a JSON body so that FastAPI Swagger can perform the OAuth2 password flow correctly.
* Updated `OAuth2PasswordBearer` configuration so Swagger automatically handles token authentication.
* Added CORS middleware to `main.py` to allow requests from a React frontend running on `localhost:3000`.
* Updated `get_current_user` dependency to decode the JWT token and fetch the corresponding user record from the database instead of returning only the username.
* Added a protected `/profile` endpoint that returns authenticated user information (`id`, `username`, `email`) for frontend testing.

**Purpose of Changes**

These updates allow the project to:

* Work properly with Swagger’s **Authorize** functionality.
* Allow a **React frontend** to authenticate and call the API without CORS issues.
* Demonstrate **JWT verification with a real protected endpoint**.
* Return full user information for authenticated requests.

**Authentication Flow After Changes**

1. User registers using `/register`.
2. User logs in using `/login` (OAuth2 password form).
3. API returns a JWT access token.
4. Client stores the token.
5. Client sends requests with `Authorization: Bearer <token>`.
6. `get_current_user` decodes the token and retrieves the user from the database.
7. Protected endpoints (such as `/profile`) return user-specific data.

**Files Updated**

* `app/api/auth_routes.py`

  * Login route now uses `OAuth2PasswordRequestForm`
  * Added `/profile` protected route

* `app/dependencies/auth_dependencies.py`

  * JWT decoding logic
  * Database lookup for authenticated user

* `app/main.py`

  * Added `CORSMiddleware`
  * Allowed React development origins (`localhost:3000`)

**Current State of Authentication System**

The API now supports:

* user registration
* OAuth2-compatible login
* JWT access tokens
* protected routes
* profile endpoint for frontend testing
* React-compatible CORS configuration

This establishes a **complete minimal JWT authentication flow** suitable for frontend integration testing.
