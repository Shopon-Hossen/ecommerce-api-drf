from django.db import models
from account.models import User
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops")
    description = models.TextField(blank=True)
    logo = models.ImageField(default=settings.DEFAULT_SHOP_LOGO_IMAGE, upload_to="image/shop/logo/")
    banner = models.ImageField(default=settings.DEFAULT_SHOP_BANNER_IMAGE, upload_to="image/shop/banner/")
    location = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
