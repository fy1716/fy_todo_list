#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/11 9:17
__author__ = 'Peter.Fang'

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
