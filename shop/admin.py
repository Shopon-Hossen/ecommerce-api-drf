from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    ordering = ("-id",)


admin.site.register(Shop, ShopAdmin)
