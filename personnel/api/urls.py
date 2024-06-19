from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    path('v1/', views.ApiListPersonnel.as_view()),
]
