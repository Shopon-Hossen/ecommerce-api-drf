import os
import django

# Set the settings module (update this with your project's settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce.settings")

# Initialize Django
django.setup()

import json
from account.models import User

# Load user data from the JSON file
with open("dummy/users.json", "r") as file:
    user_data = json.load(file)

users = []  # List to store User instances

for user_dict in user_data:
    email = user_dict.get('email')
    first_name = user_dict.get('first_name')
    last_name = user_dict.get('last_name')

    # Create User instance but don't save yet
    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_active=True,
        is_verify=True
    )
    
    # Hash the password properly
    user.set_password("1")  # Replace "1" with a secure password
    users.append(user)

# Bulk create users (faster than saving one by one)
User.objects.bulk_create(users)

print("User import completed successfully!")
