# FastAPI Blog - Full-Stack Deployed Web App

[Live Application](http://172.238.168.32)  
[GitHub Repository](https://github.com/Mollytutu/FastAPI-Deployment)

A production-minded full-stack blog application built with FastAPI. It includes server-rendered pages, REST API endpoints, user authentication, profile image uploads, password reset emails, database migrations, tests, Docker support, and VPS deployment notes.

This project demonstrates the full path from application code to a deployed web app: backend architecture, database modeling, frontend templates, authentication, file handling, testing, containerization, and Linux server deployment.

## What I Built

- Full-stack blog interface with HTML templates, CSS, and JavaScript
- REST API for users, posts, authentication, profile pictures, and pagination
- User registration, login, account management, and password changes
- JWT authentication with protected routes
- Secure password hashing with Argon2 through `pwdlib`
- Password reset flow with expiring reset tokens and email delivery
- Async database access with SQLAlchemy 2.x
- Alembic migrations for schema changes
- Profile picture processing with Pillow
- Optional AWS S3 storage for uploaded profile images
- Health check endpoint for deployment monitoring
- HTTP security headers for production use
- Automated tests for user and post workflows
- Dockerfile and VPS deployment notes for taking the app online

## Tech Stack

**Backend**

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x async ORM
- Alembic
- Pydantic and Pydantic Settings
- PyJWT
- Argon2 password hashing with `pwdlib`

**Frontend**

- Jinja2 templates
- HTML
- CSS
- JavaScript
- Static assets and web app icons

**Database and Storage**

- PostgreSQL for production
- SQLite support for local development/testing
- AWS S3 support with `boto3`
- Pillow for image validation and resizing

**Email and Auth**

- OAuth2 password login flow
- JWT bearer tokens
- SMTP email support with `aiosmtplib`
- Secure password reset tokens

**Testing and Deployment**

- Pytest
- Moto for AWS-related tests
- Docker
- uv dependency management
- Ubuntu VPS deployment
- Nginx reverse proxy notes
- systemd service notes
- Health check endpoint at `/health`

## Project Structure

```text
.
├── main.py                 # FastAPI app, page routes, middleware, health check
├── routers/                # API routers for users and posts
├── models.py               # SQLAlchemy models
├── schemas.py              # Pydantic request/response schemas
├── database.py             # Async database engine and session setup
├── auth.py                 # Password hashing, JWTs, current-user dependency
├── config.py               # Environment-based app settings
├── email_utils.py          # Password reset email delivery
├── image_utils.py          # Profile image processing and upload helpers
├── templates/              # Server-rendered HTML pages
├── static/                 # CSS, JavaScript, icons, and images
├── alembic/                # Database migrations
├── tests/                  # User and post tests
├── Dockerfile              # Production container build
└── vps_setup.txt           # VPS deployment and hardening notes
```

## Core API Routes

**Users**

- `POST /api/users` - create a user
- `POST /api/users/token` - log in and receive a JWT
- `GET /api/users/me` - get the authenticated user
- `PATCH /api/users/{user_id}` - update account information
- `DELETE /api/users/{user_id}` - delete account
- `PATCH /api/users/{user_id}/picture` - upload profile picture
- `DELETE /api/users/{user_id}/picture` - remove profile picture
- `POST /api/users/forgot-password` - request password reset email
- `POST /api/users/reset-password` - reset password with token
- `PATCH /api/users/me/password` - change password while logged in

**Posts**

- `GET /api/posts` - list paginated posts
- `GET /api/posts/{post_id}` - get one post
- `POST /api/posts` - create a post
- `PUT /api/posts/{post_id}` - replace a post
- `PATCH /api/posts/{post_id}` - partially update a post
- `DELETE /api/posts/{post_id}` - delete a post

**Pages**

- `GET /` - home page
- `GET /posts` - posts page
- `GET /posts/{post_id}` - single post page
- `GET /users/{user_id}/posts` - user posts page
- `GET /login` - login page
- `GET /register` - registration page
- `GET /account` - account page
- `GET /forgot-password` - forgot password page
- `GET /reset-password` - reset password page

## Environment Variables

Create a `.env` file in the project root for local development.

```env
SECRET_KEY=change_me
DATABASE_URL=sqlite+aiosqlite:///./app.db

MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your_username
MAIL_PASSWORD=your_password
MAIL_FROM=noreply@example.com
MAIL_USE_TLS=true
FRONTEND_URL=http://localhost:8000

S3_BUCKET_NAME=
S3_REGION=us-east-2
S3_ACCESS_KEY_ID=
S3_SECRET_ACCESS_KEY=
S3_ENDPOINT_URL=
```

Do not commit real secrets.

## Run Locally

Install dependencies with `uv`:

```bash
uv sync
```

Run migrations:

```bash
uv run alembic upgrade head
```

Start the application:

```bash
uv run fastapi dev main.py
```

Open:

```text
http://127.0.0.1:8000
```

## Run Tests

```bash
uv run pytest
```

## Docker

Build the image:

```bash
docker build -t fastapi-blog .
```

Run the container:

```bash
docker run --env-file .env -p 8080:8080 fastapi-blog
```

## Deployment

The project is currently deployed online at:

```text
http://172.238.168.32
```

Deployment work covered in this repository includes:

- Linux VPS setup
- SSH hardening
- UFW firewall configuration
- Fail2Ban setup
- Nginx reverse proxy planning
- systemd service planning
- production environment variables
- PostgreSQL-ready database configuration
- Docker production build
- `/health` endpoint for service checks

## Why This Project Matters

This is not only a FastAPI API. It is a full-stack deployed application that shows I can build the backend, connect the database, create user-facing pages, handle authentication, process uploads, write tests, prepare production configuration, and get the project online.
