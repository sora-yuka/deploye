from rest_framework.permissions import BasePermission

class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if owner.is_authenticated == (request.user.is_stuff and request.obj):
            return True