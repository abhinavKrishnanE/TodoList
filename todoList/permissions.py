from rest_framework.permissions import BasePermission


class WhichUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        
        return super().has_permission(request, view)