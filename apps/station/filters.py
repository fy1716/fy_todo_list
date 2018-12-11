#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/11 14:29
__author__ = 'Peter.Fang'

import django_filters

from .models import Station


class StationFilter(django_filters.rest_framework.FilterSet):
    '''
    站点过滤的类
    '''
    pass