from rest_framework import viewsets
from rest_framework import permissions
from .models import UserAcc
from .serializers import UserAccSerializer


class UserAccViewSet(viewsets.ModelViewSet):
    queryset = UserAcc.objects.all()
    serializer_class = UserAccSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
