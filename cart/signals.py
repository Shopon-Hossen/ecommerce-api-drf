# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from .models import Cart
from django.conf import settings


@receiver(post_save, sender=User)
def create_cart_on_user_create(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)