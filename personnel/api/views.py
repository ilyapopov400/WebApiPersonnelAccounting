from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from app.models import ProfilePersonnelModel
from . import serializers
from . import permissions


# Create your views here.

class ApiPersonnelPublic(viewsets.ModelViewSet):
    """
    Публичный (без картинок)
    Список всех карточек
    Создание новой карточки
    Получение одну карточки
    Изменение одну карточки
    Удаление одной карточки
    """
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializerPublic
    permission_classes = (AllowAny,)


class ApiPersonnelPrivate(viewsets.ModelViewSet):
    """
    Приватный (с картинками)
    Список всех карточек
    Создание новой карточки
    Получение одну карточки
    Изменение одну карточки
    Удаление одной карточки
    """
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializerPrivate
    permission_classes = (permissions.IsRegisterReadOnly,)


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
