from django.db import models
from django.core.validators import MaxLengthValidator
from product.models import Product
from account.models import User


class Comment(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    content = models.CharField(validators=[MaxLengthValidator(2000)])

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.first_name} - {self.content[:20]}'

    @property
    def is_parent(self):
        return self.parent is None
