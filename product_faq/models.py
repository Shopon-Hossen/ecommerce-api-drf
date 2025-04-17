from django.db import models
from product.models import Product


class ProductFAQ(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return f"FAQ: {self.product.name}"