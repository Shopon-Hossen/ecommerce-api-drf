from rest_framework import permissions


class IsVerifiedUser(permissions.BasePermission):
    """
    Allows access to non-safe methods only if the user is verified.
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for anyone.
        if request.method in permissions.SAFE_METHODS:
            return True
        # For non-safe methods, user must be authenticated and verified.
        return bool(request.user and request.user.is_authenticated and request.user.is_verify)
