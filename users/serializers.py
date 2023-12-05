from rest_framework.schemas.coreapi import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ["email", "first_name", "last_name"]


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserDetailSerializer.Meta.fields + [
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        ]
