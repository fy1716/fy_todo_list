from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .models import Station
from .serializers import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
