# validates.py
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models.fields.files import ImageFieldFile


def image_max_size_validate(image: ImageFieldFile):
    if image.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"Image size should not exceed {settings.MAX_UPLOAD_SIZE}MB.")

def image_max_res_validate(image: ImageFieldFile):
    if image.width > settings.MAX_IMAGE_WIDTH or image.height > settings.MAX_IMAGE_HEIGHT:
        raise ValidationError(f"Image res should not exceed {settings.MAX_IMAGE_WIDTH}x{settings.MAX_IMAGE_HEIGHT}")
