#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 10:35
__author__ = 'Peter.Fang'

import uuid

from . import config

df_config = config.df_config


def df_uuid_hex():
    return uuid.uuid1().hex
