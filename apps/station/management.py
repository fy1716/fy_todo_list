#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 10:52
__author__ = 'Peter.Fang'
from django.db.models.signals import post_migrate
from .models import Station


# 定义receiver函数
def init_db(sender, **kwargs):
    # 当发送信号的模型是你要初始化的模型的时候，在进行数据库操作，不加判断的话，每一个模型都会调用
    if sender.name == 'apps.station':
        if not Station.objects.exists():
            Station.objects.create(name='yydf', hot_line='4225875')


post_migrate.connect(init_db)
