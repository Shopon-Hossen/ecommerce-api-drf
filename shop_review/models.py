from django.db import models
from shop.models import Shop
from account.models import User


class Rating(models.TextChoices):
    BAD = "1", "Bad"
    AVERAGE = "2", "Average"
    GOOD = "3", "Good"
    VERY_GOOD = "4", "Very Good"
    EXCELLENT = "5", "Excellent"


class ShopReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="reviews")
    rating = models.CharField(
        max_length=1, 
        choices=Rating.choices,  # Choices from TextChoices
        default=Rating.GOOD  # Default rating
    )
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} rated {self.shop.name} as {self.get_rating_display()}"