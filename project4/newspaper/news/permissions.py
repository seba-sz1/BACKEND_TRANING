from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """check user if owner"""
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS --> ("GET", 'OPTIONS', "HEAD")
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.owner