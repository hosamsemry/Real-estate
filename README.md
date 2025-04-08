# Real Estate Listings API
This is a Django REST Framework-based backend project for a real estate listing platform. It provides secure authentication using JWT, custom user roles (buyers and realtors), property listings, and search functionality.

## 🚀 Features
- 🔐 JWT Authentication (rest_framework_simplejwt)
- 🧑‍💼 Custom User Model with Realtor Role
- 📋 CRUD operations for property listings
- 🔎 Full-text search on listings (PostgreSQL)
- 🧭 Multi-database support for users and listings
- 🛡️ Permissions and role-based access control
- 🗂️ Media uploads for listing images
---
## 🏗️ Tech Stack
- Python 
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT for auth
---
## API Endpoints
### 🔑 Authentication
- `POST /api/token/` – Get access and refresh tokens
- `POST /api/token/refresh/` – Refresh access token
- `POST /api/token/verify/` – Verify token validity

### 👥 User Endpoints
- `POST /api/user/register/` – Register new users or realtors
- `GET /api/user/me/` – Retrieve current user data (auth required)

## 🏘️ Listing Endpoints

| Method | Endpoint                    | Description                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/api/listing/`             | Get all published listings             |
| GET    | `/api/listing/detail/?slug=`| Get single listing by slug             |
| GET    | `/api/listing/search/?search=`| Search listings by title & description |
| POST   | `/api/listing/manage/`      | Create a new listing (realtors only)   |
| PUT    | `/api/listing/manage/?slug=`| Update a listing (realtors only)       |
| PATCH  | `/api/listing/manage/?slug=`| Partially update listing (realtors only)|
| DELETE | `/api/listing/manage/?slug=`| Delete listing (realtors only)         |

---

## 📦 Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/real-estate-backend.git
    cd real-estate-backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL databases (`users`, `listing`) and update `DATABASES` config in `settings.py`.

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```
---

Feel free to reach out for contributions or questions!
