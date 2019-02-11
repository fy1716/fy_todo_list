#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 17:19
__author__ = 'Peter.Fang'
from collections import namedtuple

_DEGREE_MAP = namedtuple('DEGREE_MAP', ['low', 'middle', 'high'])
_dm = _DEGREE_MAP(1, 2, 3)

df_config = {
    "PLATFORM_NAME": "通用管理平台",
    "TASK_COUNT": 5,
    "DEGREE_MAP": _dm
}
