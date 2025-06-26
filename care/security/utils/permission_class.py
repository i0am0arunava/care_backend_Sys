from rest_framework.permissions import BasePermission


class CareAuthentication(BasePermission):
    """
    Calls a method in the class to check if the user has access
    """

    def has_permission(self, request, view):
        if hasattr(view, "permissions_controller"):
            return view.permissions_controller(request)
        return True
