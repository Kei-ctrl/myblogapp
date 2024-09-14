from rest_framework import serializers # type: ignore
from .models import Attraction

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'name', 'description', 'latitude', 'longitude']

