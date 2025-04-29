from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from account.validates import (
    image_max_size_validate,
)
from .utlis import product_image_upload_path
from shop.models import Shop
from account.models import User
from django.contrib.postgres.indexes import GinIndex
from notification.models import UserNotification



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    # Basic Fields
    shop = models.ForeignKey(Shop, models.CASCADE, related_name="products")
    name = models.CharField(max_length=300)
    name_slug = models.SlugField(blank=True)
    description = models.TextField(default="", max_length=10**4)

    # Pricing
    price = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(10**8)])
    discount_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    cash_on_delivery = models.BooleanField(default=False)
    replacement = models.PositiveIntegerField(default=0)

    # Media
    image = models.ImageField(
        upload_to=product_image_upload_path,
        default=settings.DEFAULT_PRODUCT_IMAGE,
        validators=[image_max_size_validate]
    )

    # Other
    category = models.ForeignKey(Category, models.CASCADE, related_name='products')
    specification = models.JSONField(default=dict)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name_slug = f"{slugify(self.name)}"
        self.is_available = self.stock > 0
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            GinIndex(name="product_name_gin", fields=["name"], opclasses=["gin_trgm_ops"])
        ]


class Rating(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="rating")
    user = models.ForeignKey(User, models.CASCADE, related_name="rating")
    content = models.TextField(default="", max_length=10**3)
    star = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    create_at = models.DateTimeField(auto_now_add=True)
