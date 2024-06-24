from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.SimpleRouter()  # создание роутера
router.register(r"", views.ApiPersonnel)  # регистрация роутера

urlpatterns = [
    path('v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/
]
