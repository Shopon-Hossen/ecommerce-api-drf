from django.contrib import admin
from .models import (
    Product,
    Category,
    Comment,
    Rating
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock", "shop"]
    list_display_links = ["name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
