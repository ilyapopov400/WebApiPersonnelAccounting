from django.shortcuts import render
from rest_framework import generics, viewsets

from app.models import ProfilePersonnelModel
from . import serializers


# Create your views here.

class ApiPersonnel(viewsets.ModelViewSet):
    """
    Список всех карточек
    Создание новой карточки
    Получение одну карточки
    Изменение одну карточки
    Удаление одной карточки
    """
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializer

# class ApiCreatePersonnel(generics.ListCreateAPIView):
#     """
#     Список всех карточек
#     Создание новой карточки
#     """
#     queryset = ProfilePersonnelModel.objects.all()
#     serializer_class = serializers.ProfilePersonnelSerializer
#
#
# class ApiDetailPersonnel(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Получить одну карточку
#     изменить одну карточку
#     удалить одну карточку
#
#     """
#     queryset = ProfilePersonnelModel.objects.all()
#     serializer_class = serializers.ProfilePersonnelSerializer
