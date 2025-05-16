from django.contrib import admin
from .models import RequestUserVerify


class RequestUserVerifyAdmin(admin.ModelAdmin):
    ordering = ["create_at"]


admin.site.register(RequestUserVerify, RequestUserVerifyAdmin)