from rest_framework import serializers 
from .models import Sonu

class SonuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sonu
        fields=["name","age","email","created_at"]
        read_only_fields=["created_at"]