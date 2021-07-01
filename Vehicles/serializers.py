from rest_framework import serializers
from .models import vehicle

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'