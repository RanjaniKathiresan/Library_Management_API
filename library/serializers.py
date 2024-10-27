from rest_framework import serializers
from library.models import Users

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'