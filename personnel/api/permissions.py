from rest_framework import permissions


class IsRegisterReadOnly(permissions.BasePermission):
    """
    Проверяет, что пользователь - администратор (с правами администратора)
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
