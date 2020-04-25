from rest_framework import serializers

from core.rest_framework.serializers import ServiceSeralizer
from users.models import User


class UserSerializer(ServiceSeralizer):
    picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ["id", "email", "password", "picture"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }
