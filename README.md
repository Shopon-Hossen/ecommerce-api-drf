# 🛒 E-Commerce API (Django Rest Framework)

This is a backend API for an e-commerce platform built using Django Rest Framework (DRF). It provides authentication, products management, user profile management, image handling, Postgres Database, advance search with pg_trgm, shop management and more.

## 📌 Features

- **Account**

  - JWT auth system.
  - Custom user model with email-based login.
  - Email verification system.
  - Secure password handling.

- **User Profile Management**

  - Update user details (excluding password & email).
  - Upload/display profile pictures.
  - Old profile pictures are overwritten on update.

- **Image Handling**

  - Default profile picture when no image is provided.
  - Images larger than **5MB** are not uploaded.
  - All not used image will automatically deleted

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
  - FAQ for products.

- **Cart Management**

  - Any logged in User can add product to there cart.
  - Cart will automatically created when user register.
  - Cart items can be updated (Increment and Decrement quantity) or delete.
  - Quantity range is 1 to 99 (Can be change).

- **Real Time Notification**

  - Automatically send notification to user when UserNotification was create.


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

```psql
\c e_commerce
```

Once connected to the `e_commerce` database install the `pg_trgm` extension by running following command on `psql`

```psql
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
This will create a isolated virtual environment in `.venv` directory.

if you get some error like `python was not found or not recognized` try using `python3` or install python if not installed. 

### Install Dependencies

```bash
pip install -r requirements.txt
```
This will install all necessary packages eg django, channels etc to run our project.

### Configure Environment Variables

Create a `.env` file in the project root and add your environment variables. Example:

```bash
# Generate SECRET_KEY (Recommended)
python generate_secret_key.py
```

```
# filename: .env

ENV_STATUS = "_INFO: Development environment variable loaded successfully!"
SECRET_KEY = "django-insecure-<generate_secret_key.py output>"

EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PG_PASS = ""
```

 - The `ENV_STATUS` will help to debug does this file loaded properly.
 - `SECRET_KEY` Need to `Encrypt` and `Decrypt` data, eg `access_token` **(do not make it public)**.
 - This 2 (`EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`) variable need to sending `email`.
 - `PG_PASS` Password for PostgreSQL database.


### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

 - `makemigrations` will initialize our migrations. kind a like pack everything up before going to trip.
 - `migrate` will tell the database to changes.


### Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Then do the following. (Email, password, reenter password).
You can access the Django built in admin dashboard [**Django Admin**](http://127.0.0.1:8000/admin/)

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

- [x] Build account management system.
- [x] Implement email-based login with custom user model.
- [x] Integrate MailTrap for development email testing.
- [x] Prevent uploading excessively large files.
- [x] Create full shop management endpoints.
- [x] Integrate PostgreSQL database.
- [x] Implement `pg_trgm` extension for better search matching.
- [x] Build advanced search functionality for shops and products.
- [x] Add product filtering capabilities (e.g., price range, search by title).
- [x] Develop complete product management endpoints.
- [x] Implement product FAQ management (create, update, delete).
- [x] Build cart management (add, update, delete items).
- [x] Implement real-time user notifications using Django Channels.
- [x] Add basic security hardening (input validation, permissions, rate limiting).
- [x] Build product comment system (including replies).
- [x] Implement user-to-shop owner real-time chat (via Django Channels).
- [x] Create "Request Verification" endpoint for users.
- [x] Create "Admin Accept Verification" endpoint for verified requests.
- [x] Add real-time search recommendations (via Django Channels).
- [ ] Add unit and integration tests using **Pytest** and **DRF Test framework**.
- [ ] Learn how to Dockerize the project for easier deployment.
- [ ] Write a clean, detail API documentation for all endpoints.
- [ ] (Optional) Deploy to cloud platform (e.g., Railway, Render, or VPS) to showcase the live API.


## 📜 License

This project is licensed under a **Proprietary License**.  
🔹 **You may review the code but cannot use it in any project without permission.**  
🔹 For inquiries, contact [extremeediting572@gmail.com].

## 📧 Contact

For questions, feel free to reach out!

## **👤 Author**

- **[Shopon Hossen](https://github.com/Shopon-Hossen)**
- **[Shopon Hossen/eCommerce-API](https://github.com/Shopon-Hossen/ecommerce-api-drf)**
