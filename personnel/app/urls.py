from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('list_personnel/', views.ListPersonnel.as_view(), name='list_personnel'),  # просмотр всего персонала
    path('detail_personnel/<int:pk>', views.DetailPersonnel.as_view(), name='detail_personnel'),
    # карточка одного сотрудника
    path('create_houses/', views.CreatePersonnel.as_view(), name='create_personnel'),  # добавить в БД нового сотрудника
]
