# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/23
@desc:
"""

import os
import logging
import logging.config

# todo config
# logging_conf_file = os.path.join( 'config_script', 'logger.init')
logging_conf_file = os.path.join(
    'config', 'log', 'logger.init'
)


class LoggerConfig(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LoggerConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        path = logging_conf_file  # 默认配置日志路径
        if not os.path.exists('logs'):
            os.makedirs('logs')
        logging.config.fileConfig(path, disable_existing_loggers=False)



LoggerConfig()

debug_log = logging.getLogger('debug_log')
dblog = logging.getLogger('dblog')
