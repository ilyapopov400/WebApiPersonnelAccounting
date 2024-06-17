from django import forms
from . import models


class PersonnelForm(forms.ModelForm):
    """
    Форма для записи карточки сотрудника
    """

    class Meta:
        model = models.ProfilePersonnel
        fields = "__all__"
        labels = {
            "surname": "фамилия",
            "name": "имя",
            "patronymic": "отчество",
            "image": "фото сотрудника",
        }
        error_messages = {
            "surname": {
                "max_length": "слишком длинная фамилия",
                "min_length": "слишком короткая фамилия",
                "required": "поле не должно быть пустым",
            },
            "name": {
                "max_length": "слишком длинное имя",
                "min_length": "слишком короткое имя",
                "required": "поле не должно быть пустым",
            },
            "patronymic": {
                "max_length": "слишком длинное отчество",
                "min_length": "слишком короткое отчество",
                "required": "поле не должно быть пустым",
            },
        }
