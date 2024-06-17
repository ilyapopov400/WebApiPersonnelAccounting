from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class ProfilePersonnel(models.Model):
    """
    Класс для хранения данных о персонале
    """
    surname = models.CharField(max_length=20, verbose_name="фамилия", blank=False,
                               validators=[MinLengthValidator(2)])  # валидация минимальной длинны
    name = models.CharField(max_length=20, verbose_name="имя", blank=True, default="неизвестно",
                            validators=[MinLengthValidator(2)])  # валидация минимальной длинны
    patronymic = models.CharField(max_length=20, verbose_name="отчество", blank=True, default="неизвестно",
                                  validators=[MinLengthValidator(2)])  # валидация минимальной длинны
    image = models.FileField(upload_to="personnel_gallery/", blank=True, verbose_name="фото сотрудника")

    def __str__(self):
        return 'Profile for user {}'.format(self.surname)
