# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User
from django.conf import settings


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    return 
    if created:
        send_mail(
            subject="Welcome!",
            message="Thanks for signing up!, Verifications email will be sent",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email]
        )
