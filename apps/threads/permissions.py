from rest_framework import permissions


class IsMessageSenderOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the sender to edit or delete the message.
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods like GET are always allowed
        user = request.user

        # full permissions for admin
        if user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the sender can update or delete
        return obj.sender == request.user
