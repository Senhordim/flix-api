from rest_framework import permissions

class GenrePermission(permissions.BasePermission):
    def has_permission(self, request, view):
       return true

    def has_object_permission(self, request, view, obj):
      pass
