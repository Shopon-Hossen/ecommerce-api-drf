# validates.py
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models.fields.files import ImageFieldFile


def image_max_size_validate(image: ImageFieldFile):
    if image.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"Image size should not exceed {settings.MAX_UPLOAD_SIZE}MB.")
