# Webinar Management API

Backend REST API untuk Webinar Management Platform.

## Tech Stack

- Python 3.13
- FastAPI
- Docker
- Swagger

## Current Version

v0.1.0

## Features

- ✅ Dockerized FastAPI
- ✅ Swagger Documentation
- ✅ Health Check Endpoint
- ✅ Project Foundation

## Run

```bash
docker compose up -d
```

## API Documentation

```
http://localhost:8000/docs
```

## Authentication

- JWT Authentication
- Password Hashing
- OAuth2 Password Flow

## Authorization

- Role Based Access Control
- Admin
- Student

### Protected Endpoints

GET /users        -> Admin Only
POST /users       -> Admin Only
GET /auth/me      -> Authenticated User
