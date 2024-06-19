from django.shortcuts import render
from rest_framework import generics

from app.models import ProfilePersonnelModel
from . import serializers


# Create your views here.


class ApiListPersonnel(generics.ListAPIView):
    queryset = ProfilePersonnelModel.objects.all()
    serializer_class = serializers.ProfilePersonnelSerializer
