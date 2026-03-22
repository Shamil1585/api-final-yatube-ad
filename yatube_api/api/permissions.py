from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем чтение всем, создание только авторизованным
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение всем, изменение только автору
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
