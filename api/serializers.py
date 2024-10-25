from rest_framework import serializers
from .models import ConversionModel

class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionModel
        fields ="__all__"