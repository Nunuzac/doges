from rest_framework import permissions
from doges.models import Role

class IsOwnUserData(permissions.BasePermission):

    def has_permission(self, request, view):
        is_root = request.path == '/user/'
        if request.method in ['POST', 'OPTIONS'] or not is_root:
            return True
        if request.user.is_anonymous or not request.user.is_authenticated:
            return False
        return self.__is_from_admin(request)
        
    def has_object_permission(self, request, view, obj):
        if self.__is_from_admin(request):
            return True
        return obj.id == request.user.id

    def __is_from_admin(self, request):
        try:
             Role.objects.get(pk=request.user.role_id).name == 'admin'
        except:
            return False