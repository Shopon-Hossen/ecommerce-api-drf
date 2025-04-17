from django.db import models
from account.models import User
from django.conf import settings
from django.contrib.postgres.indexes import GinIndex


class Shop(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops")
    description = models.TextField(blank=True, max_length=10**4)
    logo = models.ImageField(default=settings.DEFAULT_SHOP_LOGO_IMAGE, upload_to="image/shop/logo/")
    banner = models.ImageField(default=settings.DEFAULT_SHOP_BANNER_IMAGE, upload_to="image/shop/banner/")
    location = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            GinIndex(name="shop_name_gin", fields=["name"], opclasses=["gin_trgm_ops"])
        ]


class PinnedShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pinned_shops")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="pinned_by_users")  
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        unique_together = ("user", "shop")  # ✅ Prevents duplicate pinning of the same shop

    def __str__(self):
        return f"{self.user.email} pinned {self.shop.name}"
