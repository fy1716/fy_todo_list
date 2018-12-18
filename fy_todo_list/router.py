#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/10 15:39
__author__ = 'Peter.Fang'

from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, GroupViewSet, PermissionListViewSet
from apps.todo_list.views import ItemsViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'permission', PermissionListViewSet)
router.register(r'items', ItemsViewSet)
