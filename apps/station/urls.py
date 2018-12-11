#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 11:20
__author__ = 'Peter.Fang'

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from . import views

router = DefaultRouter()
router.register(r'', views.StationViewSet)

urlpatterns = [
    re_path('docs/', include_docs_urls(title="Station")),
    re_path('api/', include(router.urls)),
]
