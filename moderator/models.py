from django.db import models
from account.models import User


class RequestUserVerify(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    accepted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
