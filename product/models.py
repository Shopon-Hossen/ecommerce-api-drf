from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from .validates import (
    image_max_res_validate,
    image_max_size_validate,
)
from .utlis import product_image_upload_path
from shop.models import Shop


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    # Basic Fields
    shop = models.ForeignKey(Shop, models.CASCADE, related_name="products")
    name = models.CharField(max_length=300)
    name_slug = models.SlugField(blank=True)
    description = models.TextField(default="")

    # Pricing
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    discount_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    cash_on_delivery = models.BooleanField(default=False)
    replacement = models.PositiveIntegerField(default=0)

    # Media
    image = models.ImageField(
        upload_to=product_image_upload_path,
        default=settings.DEFAULT_PRODUCT_IMAGE,
        validators=[image_max_res_validate, image_max_size_validate]
    )

    # Other
    category = models.ForeignKey(Category, models.CASCADE, related_name='products')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name_slug = f"{slugify(self.name)}"
        self.is_available = self.stock > 0
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="rating")
    content = models.TextField(default="")
    star = models.PositiveIntegerField(validators=[MaxValueValidator(5)])


class Comment(models.Model):
    # Essential
    product = models.ForeignKey(Product, models.CASCADE, related_name="comments")
    content = models.CharField()
    
    # Date and time
    create_at = models.DateTimeField(auto_now_add=True)