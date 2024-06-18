from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('list_personnel/', views.ListPersonnel.as_view(), name='list_personnel'),  # просмотр всего персонала
    path('detail_personnel/<int:pk>', views.DetailPersonnel.as_view(), name='detail_personnel'),
    # карточка одного сотрудника
    path('create_personnel/', views.CreatePersonnel.as_view(), name='create_personnel'),
    # добавить в БД нового сотрудника
    path('update_personnel/<int:pk>', views.UpdatePersonnel.as_view(), name='update_personnel'),
    # изменить в БД карточку сотрудника
    path('delele_personnel/<int:pk>', views.DeletePersonnel.as_view(), name='delete_personnel'),
    # удалить из БД карточку сотрудника
]
