from rest_framework import permissions


class ObjectIsRequestUser(permissions.BasePermission):
    def has_object_permisson(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
