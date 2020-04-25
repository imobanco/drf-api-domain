from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAuthenticatedOrCreate(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == "POST"


class IsAdmin(BasePermission):
    """
    Object-level permission to only admins
    to view objects.
    """

    def has_object_permission(self, request, view, obj):
        return view.action == "retrieve" and request.user.is_superuser


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners
    of an object to edit or view it.
    Assumes the model instance has an `user_owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user_owner == request.user


class IsOwnerOrAdmin(IsOwner, IsAdmin):
    """
    Object-level permission to only allow owners of an object
    to edit or view it.
    If user is superuser it allows view methods.
    """

    def has_object_permission(self, request, view, obj):
        return IsOwner.has_object_permission(
            self, request, view, obj
        ) or IsAdmin.has_object_permission(self, request, view, obj)


class IsParticipant(BasePermission):
    """
    Object-level permission to only allow participants
    of an object to view it.
    Assumes the model instance has an `user_participants` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return view.action == "retrieve" and request.user in obj.user_participants


class IsParticipantOrAdmin(IsParticipant, IsAdmin):
    """
    Object-level permission to only allow participants
    of an object to view it.
    Assumes the model instance has an `user_participants` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return IsParticipant.has_object_permission(
            self, request, view, obj
        ) or IsAdmin.has_object_permission(self, request, view, obj)


class IsOwnerOrAdminOrParticipantReadOnly(IsParticipant, IsOwner, IsAdmin):
    """
    Object-level permission to only allow owners of an object
    to edit or view it.
    Allows read!
    """

    def has_object_permission(self, request, view, obj):
        return (
            IsOwner.has_object_permission(self, request, view, obj)
            or IsParticipant.has_object_permission(self, request, view, obj)
            or IsAdmin.has_object_permission(self, request, view, obj)
        )
