from rest_framework import serializers

from app.models import ProfilePersonnelModel


class ProfilePersonnelSerializerPublic(serializers.ModelSerializer):
    """
    Публичный сереалайзер
    """
    class Meta:
        model = ProfilePersonnelModel
        fields = ("id", "surname", "name", "patronymic",)


class ProfilePersonnelSerializerPrivate(serializers.ModelSerializer):
    """
    Приватный сереалайзер с картинками
    """
    class Meta:
        model = ProfilePersonnelModel
        fields = ("id", "surname", "name", "patronymic", "image",)
