from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class Index(TemplateView):
    '''
    Стартовая страница приложения
    '''

    template_name = "app/index.html"
