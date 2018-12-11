#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/10 15:39
__author__ = 'Peter.Fang'

from rest_framework.routers import DefaultRouter
from apps.station.views import StationViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'station', StationViewSet)
