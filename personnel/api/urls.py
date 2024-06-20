from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    path('v1/', views.ApiCreatePersonnel.as_view()),
    # path('v1/<int:pk>/', views.ApiCreatePersonnel.as_view()),
]
