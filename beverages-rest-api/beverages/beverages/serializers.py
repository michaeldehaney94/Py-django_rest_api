from rest_framework import serializers

from .models import Beverage


class BeverageSerializer(serializers.ModelSerializer):
    # metadata describing the model data
    class Meta:
        model = Beverage
        fields = ['id', 'name', 'description']
