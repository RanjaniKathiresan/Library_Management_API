from rest_framework import serializers
from library.models import Users, Books

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        read_only_fields = ['add_by']