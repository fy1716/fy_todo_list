#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/14 15:48
__author__ = 'Peter.Fang'
import re
import os
import logging
from fy_general_framework import settings


def log_init(trace, file_name):
    trace_len = len(trace)
    trace = trace[trace_len - 2][:2]
    call_name = ((trace[0].split('/'))[-1])

    path, name = os.path.split(call_name)
    dir_name = os.path.basename(path)
    logfile_head = file_name or '_'.join((dir_name, name))

    # re_obj = re.compile(r'\w*\.py?')
    # res = re_obj.findall(trace[0])
    # if len(res) == 0:
    #     logfile_head = 'un_know'
    # else:
    #     logfile_head = file_name or res[0]
    line_id = trace[1]
    log_file = settings.BASE_DIR + os.sep + 'log/' + logfile_head + '.log'

    logger = logging.getLogger(logfile_head)  # 获取logger
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file)
    # handler.setLevel(logging.INFO)

    fmt = '[%(asctime)s %(call_name)s %(line_id)d] %(levelname)s: %(message)s'

    formatter = logging.Formatter(fmt)  # 实例化formatter
    handler.setFormatter(formatter)  # 为handler添加formatter

    logger.addHandler(handler)  # 为logger添加handler

    return logger, handler, {'line_id': line_id, 'call_name': call_name}


def log_close(handle, logger):
    try:
        handle.flush()
        logger.removeHandler(handle)
        logging.shutdown()
    except Exception:
        pass
