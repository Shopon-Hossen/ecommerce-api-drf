from rest_framework import permissions


class IsShopOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for anyone.
        if request.method in permissions.SAFE_METHODS:
            return True

        # For non-safe methods, user must be authenticated and verified.
        return request.user and request.user.is_authenticated and request.user.is_verify


    def has_object_permission(self, request, view, obj):
        # Allow safe methods for anyone.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the shop user can update or delete the shop.
        return obj.user == request.user
