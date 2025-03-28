import os
from PIL import Image
from django.conf import settings


def save_dp_image(instance):
    with Image.open(instance.display_picture.path) as img:
        # Convert to RGB if it's not already.
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Generate a new filename based on the user's email and ID.
        filename = f'{instance.email}_{instance.id}.jpg'
        new_path = os.path.join('image/dp/', filename)

        # Save the image as a JPEG.
        img.save(os.path.join(settings.MEDIA_ROOT, new_path), 'JPEG')

        # Delete the originally uploaded image.
        if os.path.isfile(instance.display_picture.path):
            os.remove(instance.display_picture.path)

        instance.display_picture.name = new_path
