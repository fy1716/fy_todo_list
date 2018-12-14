#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/7 10:35
__author__ = 'Peter.Fang'

import uuid
import traceback

from . import config
from .sub.fy_log import log_close, log_init

df_config = config.df_config


def df_uuid_hex():
    return uuid.uuid1().hex


def debug(msg, file_name=''):
    logger, handler, d = log_init(traceback.extract_stack(), file_name)
    logger.debug(msg, extra=d)
    log_close(handler, logger)


def info(msg, file_name=''):
    logger, handler, d = log_init(traceback.extract_stack(), file_name)
    logger.info(msg, extra=d)
    log_close(handler, logger)
