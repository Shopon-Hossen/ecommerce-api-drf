from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "is_active", )
    list_filter = ("is_active", "is_staff", )
    search_fields = ("email", "first_name")
    ordering = ("-id",)


admin.site.register(User, UserAdmin)
