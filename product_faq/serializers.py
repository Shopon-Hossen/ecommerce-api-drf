# serializers.py
from rest_framework import serializers
from .models import ProductFAQ


class ProductFAQSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ProductFAQ
        fields = ["id", "product", "question", "answer"]
        read_only_fields = ["id"]
