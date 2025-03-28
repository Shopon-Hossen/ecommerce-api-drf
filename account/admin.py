from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email",  "first_name", "id",  "is_active", "is_verify")
    list_display_links = ("email", )
    list_filter = ("is_active", "is_staff", )
    search_fields = ("email", "first_name")
    ordering = ("-id",)


admin.site.register(User, UserAdmin)
