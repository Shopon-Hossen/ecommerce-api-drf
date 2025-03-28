from rest_framework import permissions


class IsShopOwner(permissions.BasePermission):
    """
    Allows access only to the owner of the shop.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods for anyone.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the shop owner can update or delete the shop.
        return obj.owner == request.user
