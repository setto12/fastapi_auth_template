# FastAPI JWT Auth Template

A reusable authentication module for FastAPI projects using JWT tokens.\
This project is designed as a learning-friendly reference implementation
that can also be reused in other APIs.

## Features

-   FastAPI authentication system
-   JWT access tokens
-   Password hashing with Passlib + Argon2
-   Modular project architecture
-   SQLAlchemy user model
-   Dependency-based route protection
-   Environment configuration with `pydantic-settings`

## Tech Stack

-   FastAPI
-   SQLAlchemy
-   Passlib (argon2)
-   python-jose
-   pydantic-settings
-   Uvicorn

## Project Structure

    fastapi-auth-template/
    │
    ├── app/
    │   ├── main.py
    │   │
    │   ├── core/
    │   │   ├── config.py
    │   │   └── security.py
    │   │
    │   ├── db/
    │   │   ├── database.py
    │   │   └── models.py
    │   │
    │   ├── schemas/
    │   │   └── auth_schema.py
    │   │
    │   ├── services/
    │   │   └── auth_service.py
    │   │
    │   ├── api/
    │   │   └── auth_routes.py
    │   │
    │   └── dependencies/
    │       └── auth_dependencies.py
    │
    └── requirements.txt

## Setup Instructions

### 1. Clone or Copy the Project

    git clone <repo>
    cd fastapi-auth-template

### 2. Create a Virtual Environment

    python -m venv env
    source env/bin/activate

Windows:

    env\Scripts\activate

### 3. Install Dependencies

    pip install fastapi uvicorn sqlalchemy python-jose passlib[argon2] python-multipart pydantic-settings

### 4. Create Environment File

Create `.env` in the root directory:

    SECRET_KEY=change_this_secret_key

### 5. Run the Server

    uvicorn app.main:app --reload

Server will run at:

    http://127.0.0.1:8000

## API Endpoints

### Register User

    POST /register

Example request:

    {
      "username": "testuser",
      "email": "test@email.com",
      "password": "password123"
    }

### Login

    POST /login

Response:

    {
      "access_token": "...",
      "token_type": "bearer"
    }

### Protected Routes

Use the JWT token in headers:

    Authorization: Bearer <token>

## Example Protected Endpoint

    @app.get("/profile")
    def profile(user=Depends(get_current_user)):
        return {"user": user}

## Reusing This Auth Module

To reuse in another FastAPI project:

Copy:

    core/
    dependencies/
    services/
    schemas/auth_schema.py
    api/auth_routes.py

Update:

    database.py
    models.py

## Future Improvements

-   Refresh tokens
-   Token revocation
-   Role-based access control
-   OAuth login (Google / GitHub)
-   Multi-tenant authentication
