# validates.py
from django.core.exceptions import ValidationError
from django.conf import settings


def image_max_size_validate(image):
    if image.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"Image size should not exceed {settings.MAX_UPLOAD_SIZE}MB.")

def image_max_res_validate(image):
    if image.width > settings.MAX_IMAGE_WIDTH or image.height > settings.MAX_IMAGE_HEIGHT:
        raise ValidationError(f"Image res should not exceed {settings.MAX_IMAGE_WIDTH}x{settings.MAX_IMAGE_HEIGHT}")

def image_type_validate(image):
    valid_types = ['jpeg', 'png', 'jpg']
    file_type = image.format.lower()
    if file_type not in valid_types:
        raise ValidationError("Only JPEG and PNG formats are allowed.")