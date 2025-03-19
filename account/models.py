# accounts/models.py
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import os


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # if is verified then user can create `Shop`
    is_verify = models.BooleanField(default=False)

    display_picture = models.ImageField(
        default=settings.DEFAULT_PROFILE_IMAGE_URL, blank=True, null=True, upload_to="image/dp/"
    )

    # Set email as the USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Process the image only if a custom image is provided (not the default)
        if self.display_picture and self.display_picture.name != settings.DEFAULT_PROFILE_IMAGE_URL:
            from PIL import Image

            # Save the model first to ensure we have an ID and the image is available on disk.
            super().save(*args, **kwargs)

            # Open the uploaded image.
            img = Image.open(self.display_picture.path)

            # Convert to RGB if it's not already.
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Generate a new filename based on the user's email and ID.
            filename = f'{self.email}_{self.id}.jpg'
            new_path = os.path.join('image/dp/', filename)

            # Save the image as a JPEG (you can add additional compression parameters here).
            img.save(os.path.join(settings.MEDIA_ROOT, new_path), 'JPEG')

            # Delete the originally uploaded image.
            if os.path.isfile(self.display_picture.path):
                os.remove(self.display_picture.path)

            # Update the model to point to the new processed image.
            self.display_picture.name = new_path
            super().save(update_fields=['display_picture'])

        else:
            # If no image is provided, or if it is the default image,
            # explicitly set the display_picture to the default.
            if not self.display_picture:
                self.display_picture = settings.DEFAULT_PROFILE_IMAGE_URL
            super().save(*args, **kwargs)
