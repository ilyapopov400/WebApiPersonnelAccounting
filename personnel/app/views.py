from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models
from . import forms


# Create your views here.

class Index(TemplateView):
    '''
    Стартовая страница приложения
    '''

    template_name = "app/index.html"


class ListPersonnel(ListView):
    """
    Список просмотра для всех сотрудников
    """
    template_name = "app/list_personnel.html"
    model = models.ProfilePersonnel
    context_object_name = "personnel"  # переменная, передающаяся в шаблон
    # (можно использовать по дефолту object_list)


class DetailPersonnel(DetailView):
    """
    Карточка просмотра одного сотрудника
    """
    template_name = "app/detail_personnel.html"
    model = models.ProfilePersonnel
    context_object_name = "person_one"  # переменная, передающаяся в шаблон
    # (можно использовать по дефолту object или название модели со строчной буквы)


class CreatePersonnel(CreateView):
    """
    Создать карточку для нового сотрудника
    """
    form_class = forms.PersonnelForm
    template_name = "app/create_personnel.html"
    model = models.ProfilePersonnel
    success_url = reverse_lazy("app:list_personnel")
