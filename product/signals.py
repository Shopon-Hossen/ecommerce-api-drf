# signals.py
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from notification.models import UserNotification
from .models import Product, Rating
import os
from django.conf import settings



@receiver(post_delete, sender=Product)
def delete_image_on_product_delete(sender, instance, **kwargs):
    if instance.image and (instance.image.name != settings.DEFAULT_PRODUCT_IMAGE):
        instance.image.delete(save=False)


@receiver(pre_save, sender=Product)
def delete_image_on_product_update(sender, instance, **kwargs):
    if (not instance.pk) or (instance.image.name == settings.DEFAULT_PRODUCT_IMAGE):
        return
    
    try:
        old_instance = Product.objects.get(pk=instance.pk)

    except Product.DoesNotExist:
        return
    
    old_image = old_instance.image
    new_image = instance.image

    if old_image and new_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


@receiver(post_save, sender=Rating)
def create_notification_rating_creation(sender, instance, created, **kwargs):

    if created:
        UserNotification.objects.create(
            user=instance.product.shop.user,
            message=f"[**{instance.user.first_name}**]({reverse("profile", kwargs={"pk": instance.user.pk})}) give **{instance.star}** star rating on [**{instance.product.name}**]({reverse("detail-update-delete-product", kwargs={"pk": instance.product.pk})})"
        )
