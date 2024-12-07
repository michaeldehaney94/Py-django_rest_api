from rest_framework import serializers
from .models import User


# used to convert model data into json data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
