from rest_framework import serializers

from app.models import ProfilePersonnelModel


class ProfilePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePersonnelModel
        fields = ("id", "surname", "name", "patronymic", "image",)
