from django.contrib.postgres.indexes import GinIndex
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from .image_utils import save_dp_image


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
        default=settings.DEFAULT_PROFILE_IMAGE, upload_to="image/dp/"
    )

    # Set email as the USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # If the instance already exists, check if the display_picture has changed.
        if self.pk:
            old = type(self).objects.get(pk=self.pk)
            # If the image file has not changed, skip the image processing logic.
            if old.display_picture.name == self.display_picture.name:
                return super().save(*args, **kwargs)

        # If a custom image is provided (and it's not the default image)
        if self.display_picture and self.display_picture.name != settings.DEFAULT_PROFILE_IMAGE:
            # First, save the instance so that the file is available on disk.
            super().save(*args, **kwargs)

            # Process the image (save as JPEG and delete the original)
            save_dp_image(self)

            # Save the updated image field (with new relative path)
            super().save(update_fields=['display_picture'])
        else:
            # If no image is provided, or if it is the default image, explicitly set it.
            if not self.display_picture:
                self.display_picture = settings.DEFAULT_PROFILE_IMAGE
            super().save(*args, **kwargs)

    class Meta:
        indexes = [
            GinIndex(name="user_first_name_gin", fields=["first_name"], opclasses=["gin_trgm_ops"]),
            GinIndex(name="user_last_name_gin", fields=["last_name"], opclasses=["gin_trgm_ops"]),
        ]
