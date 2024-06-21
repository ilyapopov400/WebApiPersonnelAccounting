from django.shortcuts import render
from rest_framework import generics

from app.models import ProfilePersonnelModel
from . import serializers


# Create your views here.


class ApiCreatePersonnel(generics.ListCreateAPIView):
    """
    Список всех карточек
    Создание новой карточки
    """
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializer


class ApiDetailPersonnel(generics.RetrieveUpdateDestroyAPIView):
    """
    Получить одну карточку
    изменить одну карточку
    удалить одну карточку

    """
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializer
