#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 11:19
__author__ = 'Peter.Fang'

from rest_framework import serializers
from .models import UserAcc


class UserAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcc
        fields = '__all__'
