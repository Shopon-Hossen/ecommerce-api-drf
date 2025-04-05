# signals.py
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Product
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
    