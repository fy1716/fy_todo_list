#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/18 15:50
__author__ = 'Peter.Fang'

import xadmin
from .models import *


class TypeAdmin(object):
    list_display = ["name"]


class ItemsAdmin(object):
    list_display = ["title"]


class ScheduleAdmin(object):
    list_display = ["date"]


xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Items, ItemsAdmin)
xadmin.site.register(Schedule, ScheduleAdmin)
