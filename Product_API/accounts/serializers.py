from rest_framework import serializers
from accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        u = CustomUser.objects.create_user(**validated_data)
        u.save()
        return u
