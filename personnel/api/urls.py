from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.SimpleRouter()  # создание роутера
router.register(r"public", views.ApiPersonnelPublic)  # регистрация роутера публичного (без картинок)

router_private = routers.SimpleRouter()
router_private.register(r"private", views.ApiPersonnelPrivate)  # регистрация роутера приватного (с картинками)

urlpatterns = [
    path('v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/public
    path('v1/', include(router_private.urls)),  # http://127.0.0.1:8000/api/v1/private
]
