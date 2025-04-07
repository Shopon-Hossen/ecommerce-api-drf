# 🛒 E-Commerce API (Django Rest Framework)

This is a backend API for an e-commerce platform built using Django Rest Framework (DRF). It provides authentication, products management, user profile management, image handling, Postgres Database, advance search with pg_trgm, shop management and more.

## 📌 Features

- **Account**

  - Custom user model with email-based login.
  - Email verification system.
  - Secure password handling.

- **User Profile Management**

  - Update user details (excluding password & email).
  - Upload/display profile pictures.
  - Old profile pictures are overwritten on update.

- **Image Handling**

  - Images are stored locally.
  - Default profile picture when no image is provided.
  - Images larger than **5MB** are not uploaded.
  - Prevents super high-resolution images.

- **Shop Management**

  - Create, Read, Update, Delete (CRUD) shops.
  - Fuzzy search shops (Typo correction, best match first).
  - Like/Pin any shop by any Users.

- **Product Management**

  - Product can be Create, Update, Delete if user owner of the shop.
  - Any user can see: list and detail of Products.
  - Fuzzy search products using pg_trgm.
  - Filtering product (price range, ordering).
  - Any logged in user can rate any Products.

## 🚀 Installation & Setup

### Install PostgreSQL if not installed

On `Linux` use APT to install PostgreSQL

```bash
apt install postgresql
```

On `Windows` download PostgreSQL and install it.

### Create PostgreSQL Database

Create a postgresql database with name of `e_commerce`. why `e_commerce`? A: it must be same name as in your `settings.py > DATABASES > default > NAME`

Once you have created the database now you need to install an PostgreSQL extension named `pg_trgm`. why need to install this extension? A: it help us to improve search functionality and performance.

To install `pg_trgm` extension first connect to `e_commerce` database. to do that run this command on `psql`

```bash
\c e_commerce
```

Once connected to the `e_commerce` database install the `pg_trgm` extension by running following command on `psql`

```bash
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

### Clone the Repository

```bash
git clone https://github.com/Shopon-Hossen/ecommerce-api-drf.git e_commerce
cd e_commerce
```

### Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root and add your environment variables. Example:

```bash
# Generate SECRET_KEY (Good Practice)
python generate_secret_key.py
```

```
# filename: .env
ENV_STATUS = "INFO: Development environment variable loaded successfully!"
SECRET_KEY = "django-insecure-<generate_secret_key.py output>" # Best Practice

EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PG_PASS = ""
```

### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Then do the following. (Email, password, again_password)

### Start the Development Server

```bash
python manage.py runserver
```

## 🔥 API Endpoints

```bash
# get available list of urls
python list_urls.py
```

You can test APIs with Postman client. just import `e_commerce.postman_collection.json` in your Postman collection.

## ✅ To-Do List

- [x] Add account apps ✅
- [x] Prevent to upload large files ✅
- [x] Add shop models and endpoints ✅
- [x] Implement Postgres DB ✅
- [x] Add advance search functionality ✅
- [x] Add review functionality ✅
- [x] Add product models and endpoints ✅
- [ ] Implement cart and checkout functionality

## 📜 License

This project is licensed under a **Proprietary License**.  
🔹 **You may review the code but cannot use it in any project without permission.**  
🔹 For inquiries, contact [extremeediting572@gmail.com].

## 📧 Contact

For questions, feel free to reach out!

## **👤 Author**

- **[Shopon Hossen](https://github.com/Shopon-Hossen)**
- **[Shopon Hossen/eCommerce-API](https://github.com/Shopon-Hossen/ecommerce-api-drf)**
