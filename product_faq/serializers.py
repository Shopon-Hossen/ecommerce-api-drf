# serializers.py
from rest_framework import serializers
from .models import ProductFAQ


class ProductFAQSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductFAQ
        fields = "__all__"
        read_only_fields = ["id", "product"]
