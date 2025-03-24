# 🛒 E-Commerce API (Django Rest Framework)

This is a backend API for an e-commerce platform built using Django Rest Framework (DRF). It provides authentication, user profile management, image handling, and more.

## 📌 Features

- **User Authentication**

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
  - Images larger than **2MB** are compressed. **(👩‍💻 In development)**
  - Prevents super high-resolution images. **(👩‍💻 In development)**

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shopon-Hossen/ecommerce-api-drf.git e_commerce
cd e_commerce
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add your environment variables. Example:

```bash
# Generate SECRET_KEY
python generate_secret_key.py
```

```
# filename: .env
SECRET_KEY = "<SECRET_KEY>"
EMAIL_HOST_USER = "<EMAIL_HOST_USER>"
EMAIL_HOST_PASSWORD = "<EMAIL_HOST_PASSWORD>"
```

### 5️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

---

## 🔥 API Endpoints

```python
python list_urls.py
```

---

## 📂 Project Structure [ Overview ]

```
e_commerce/
│── api/                    # API prefix
|   ...
│   ├── urls.py             # Global API routes
|
│── accounts/               # User authentication and profile management
|   ...
│   ├── models.py           # Custom User model
│   ├── serializers.py      # API data serializers
│   ├── views.py            # API views
│   ├── urls.py             # Routes for authentication & profiles
│   ├── utils.py            # Helper functions (email verification, image processing)
│
│── e_commerce/              # Main Django project directory
|   ...
│   ├── settings.py         # Django settings
│   ├── urls.py             # Global Endpoint routes
│
│── media/                  # Stores uploaded media files (profile pictures, etc.)
│── static/                 # Stores static files (javascript, css, etc.)
│
|   ...
│── .env                    # Environment variables
│── manage.py               # Django management script
│── requirements.txt        # Required Python dependencies
│── README.md               # Project documentation
```

---

## ✅ To-Do List

- [x] Add account apps ✅
- [ ] Prevent to upload large files
- [ ] Add product models and endpoints
- [ ] Implement cart and checkout functionality

---

## 📜 License

This project is open-source showcase project no license are applied.

---

## 📧 Contact

For questions, feel free to reach out!

## **👤 Author**

- **[Shopon Hossen](https://github.com/Shopon-Hossen)**
- **[Shopon-Hossen/ECommerce-API](https://github.com/Shopon-Hossen/ecommerce-api-drf)**
