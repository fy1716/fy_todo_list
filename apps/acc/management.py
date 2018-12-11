#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 10:52
__author__ = 'Peter.Fang'
from django.db.models.signals import post_migrate
from .models import UserAcc, Acc
from apps.station.models import Station


# 定义receiver函数
def init_db(sender, **kwargs):
    # 当发送信号的模型是你要初始化的模型的时候，在进行数据库操作，不加判断的话，每一个模型都会调用
    if sender.name == 'apps.acc':
        if not UserAcc.objects.exists():
            station = Station.objects.first()
            acc = Acc(name='空气滤芯', acc_id='AC2345-01', amount=30, cost=10.5)
            acc.save()
            UserAcc.objects.create(station=station, acc=acc, common_name='机油格')


post_migrate.connect(init_db)
