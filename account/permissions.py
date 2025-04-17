from rest_framework import permissions


class IsVerifiedUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for anyone.
        if request.method in permissions.SAFE_METHODS:
            return True
        # For non-safe methods, user must be authenticated and verified.
        return bool(request.user and request.user.is_authenticated and request.user.is_verify)
