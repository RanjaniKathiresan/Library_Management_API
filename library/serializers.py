from rest_framework import serializers
from library.models import Users

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
