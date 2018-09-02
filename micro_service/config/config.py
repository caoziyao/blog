# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""
from .local_dev import LocalDevConfig
from .gray_production import GrayProductionConfig
from .production import ProductionConfig


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self, mode):
        self.mode = mode
        self.config = None
        self.local_config()

    def local_config(self):
        mode = self.mode
        if mode == 'production':
            # 线上配置
            conf = ProductionConfig
        elif mode == 'gray':
            # 灰度配置
            conf = GrayProductionConfig
        else:
            # 本地开发配置
            conf = LocalDevConfig

        self.config = conf


config = Config('local_dev').config
