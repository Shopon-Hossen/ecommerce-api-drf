from django.db import models
from account.models import User
from product.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator


class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name="cart")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cart", "product"], name="unique_cart_product")
        ]
