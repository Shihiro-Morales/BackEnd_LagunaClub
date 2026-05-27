from rest_framework.permissions import BasePermission


from rest_framework.permissions import BasePermission

class SoloAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_staff
        )