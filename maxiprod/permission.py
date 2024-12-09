from rest_framework.permissions import SAFE_METHODS, BasePermission


SAFE_METHODS = ('GET', 'OPTIONS', 'HEAD')


class IsAdminOrReadyOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(

                request.method in SAFE_METHODS or (request.user and request.user.is_authenticated)
                ) 
