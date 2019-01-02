#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/17 16:42
__author__ = 'Peter.Fang'

from rest_framework import serializers
from .models import *
from util import common_util


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    type_name = serializers.SerializerMethodField()  # 增加展示的外来字段

    class Meta:
        model = Items
        fields = (
            'id', 'title', 'content', 'start_time', 'period', 'finish_flag', 'finish_degree', 'priority', 'degree',
            'item_type', 'date', 'remark', 'type_name')

    def get_type_name(self, obj):
        return obj.item_type.name


class ScheduleSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Schedule
        fields = "__all__"
