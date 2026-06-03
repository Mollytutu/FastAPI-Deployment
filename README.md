# FastAPI Application

[![GitHub Repo](https://img.shields.io/badge/GitHub-FastAPI--Deployment-blue?logo=github)](https://github.com/Mollytutu/FastAPI-Deployment)  
[Live preview](http://172.238.168.32) available temporarily while the application is being finalized.

A full-stack blog application built with FastAPI, SQLAlchemy, Jinja2 templates, JWT authentication, password reset email support, and optional AWS S3 profile image uploads.

This repository is published at `https://github.com/Mollytutu/FastAPI-Deployment`.

This project demonstrates end-to-end web application skills, including backend API design, frontend templating, database modeling, authentication, file upload handling, security hardening, testing, and deployment preparation.

## Key Features

- Full-stack blog experience with server-rendered pages and a JSON API
- JWT-based authentication for protected endpoints
- User registration, login, account profile, and password reset flows
- Secure password hashing and reset-token management
- Async SQLAlchemy with PostgreSQL / SQLite support
- Image upload and profile picture handling with optional AWS S3 integration
- Pagination for post listings
- Custom security headers and health check endpoint
- Automated tests for user and post workflows
- VPS deployment notes included in `vps_setup.txt`

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x (async)
- Jinja2 templating
- Pydantic / Pydantic Settings
- PostgreSQL / SQLite
- JWT (`pyjwt`)
- SMTP email support
- AWS S3 upload support via `boto3`
- PyTest for tests

## Project Structure

- `main.py` - FastAPI application and page routes
- `routers/` - API routers for posts and users
- `models.py` - SQLAlchemy data models
- `schemas.py` - Pydantic request/response models
- `config.py` - application settings and environment loading
- `database.py` - async database engine and session management
- `auth.py` - authentication helpers and token utilities
- `templates/` - HTML views for pages like login, register, home, posts
- `static/` - CSS, JavaScript, icons, and profile picture assets
- `tests/` - API and integration tests
- `vps_setup.txt` - deployment and VPS hardening notes

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd fastapi_project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install dependencies

Install the main dependencies manually from the project requirements.

```bash
python -m pip install fastapi[standard] aiosqlite alembic boto3 greenlet jinja2 pillow psycopg[binary] pwdlib[argon2] pydantic-settings pyjwt python-multipart sqlalchemy uvicorn
```

If you plan to run tests:

```bash
python -m pip install pytest moto httpx
```

### 4. Configure environment variables

Create a `.env` file in the project root with the required values.

Example `.env`:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql+psycopg://user:password@host/database
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your_email_username
MAIL_PASSWORD=your_email_password
MAIL_FROM=noreply@example.com
MAIL_USE_TLS=True
FRONTEND_URL=http://localhost:8000

# Optional AWS S3 configuration
S3_BUCKET_NAME=your-bucket-name
S3_REGION=us-east-2
S3_ACCESS_KEY_ID=your-access-key
S3_SECRET_ACCESS_KEY=your-secret-key
S3_ENDPOINT_URL=
```

> Do not commit `.env` or any secret values to version control.

### 5. Run the application

```bash
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000` in your browser.

## API Endpoints

### Users

- `POST /api/users` - Register a new user
- `POST /api/users/token` - Login and receive access token
- `GET /api/users/me` - Get current authenticated user
- `POST /api/users/forgot-password` - Send password reset email
- `POST /api/users/reset-password` - Reset password with token

### Posts

- `GET /api/posts` - List paginated posts
- `GET /api/posts/{post_id}` - Get a single post
- `POST /api/posts` - Create a post (authenticated)
- `PATCH /api/posts/{post_id}` - Update a post (authenticated, owner only)
- `PUT /api/posts/{post_id}` - Replace a post (authenticated, owner only)
- `DELETE /api/posts/{post_id}` - Delete a post (authenticated, owner only)

### Health Check

- `GET /health` - Application health status and database connectivity

## Testing

Run the test suite with:

```bash
pytest
```

## Deployment Notes

- This project includes `vps_setup.txt` with a reproducible VPS setup workflow for Ubuntu 24.04
- Temporary live preview is available at `http://172.238.168.32` while the application is being finalized
- The application is designed to run behind a web server or reverse proxy and supports PostgreSQL and AWS S3
- Security features include JWT authentication, secure password storage, and HTTP security headers

## Why This Project

This repository showcases real full-stack delivery skills:

- backend architecture and API design
- relational data modeling and async database access
- user authentication and authorization
- secure production-friendly configuration
- front-end templating and UX flows
- testing and deployment planning

If you want, I can also add a `.env.example` and a `requirements.txt` file to make setup even easier.