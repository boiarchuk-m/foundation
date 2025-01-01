from rest_framework import permissions

class IsManager(permissions.BasePermission):


    def has_permission(self, request, view):
        # Check if the user is authenticated and has a manager role
        return request.user.is_authenticated and request.user.role == 'manager'

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a request to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Only allow users to access their own requests
        return obj.user == request.user