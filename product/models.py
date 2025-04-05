from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from .validates import (
    image_max_res_validate,
    image_max_size_validate,
    image_type_validate
)


class Prodcut(models.Model):
    # Basic Fields
    name = models.CharField(max_length=300)
    name_slug = models.SlugField()
    description = models.TextField(default="")

    # Pricing
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    discount_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)

    # Media
    image = models.ImageField(
        upload_to="image/product/",
        default=settings.DEFAULT_PRODUCT_IMAGE,
        validators=[image_max_res_validate, image_max_size_validate, image_type_validate]
    )


    def save(self, *args, **kwargs):
        self.name_slug = f"{slugify(self.name)}"
        self.is_available = self.stock > 0
        return super().save(*args, **kwargs)