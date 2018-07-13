# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc: 日志工具类
"""
import os
import logging
import logging.config
import json
from logging import Logger
from config import option


class LoggerConfig(object):

    def __init__(self):
        path = option.logging_conf_file  # 默认配置日志路径
        logging.config.fileConfig(path)
        logger = logging.getLogger('log')  # 获取dblog的日志配置
        logger.info('init log')

LoggerConfig()

db_log = logging.getLogger('dblog')
log = logging.getLogger('log')