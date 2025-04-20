# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserNotification
from .utils import send_notification_user


@receiver(post_save, sender=UserNotification)
def notify_user_on_notification_create(sender, instance, created, **kwargs):
    if created:
        send_notification_user(instance.user.pk, instance.message)
