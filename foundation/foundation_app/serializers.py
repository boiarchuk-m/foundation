from rest_framework import serializers
from .models import CustomUser, Request

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ["id", "created_at", "author", "full_name",
                  "military_unit_number", "phone_number", "request_text", "status"]
        extra_kwargs = {"author": {"read_only": True}}

