import os
import django

# Set the settings module (update this with your project's settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce.settings")

# Initialize Django
django.setup()

import json
from shop.models import Shop
from account.models import User


# Load user data from the JSON file
with open("dummy/shops.json", "r") as file:
    data = json.load(file)

shops = []  # List to store User instances

for data_dict in data:
    name = data_dict.get('name')
    description = data_dict.get('description')
    location = data_dict.get('location')
    owner = User.objects.all().order_by('?').first()

    # Create User instance but don't save yet
    shop = Shop(
        name=name,
        description=description,
        location=location,
        owner=owner,
    )
    
    shops.append(shop)


# Bulk create users (faster than saving one by one)
Shop.objects.bulk_create(shops)

print("Shops import completed successfully!")
