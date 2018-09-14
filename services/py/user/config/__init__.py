# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

import os
from config_default.default import EnvironmentConfig
from .debug import DebugConfig
from .produ import ProductConfig


def load_config():
    env = EnvironmentConfig()
    mode = env.APP_ENV
    if mode == 'produ':
        config = ProductConfig
    else:
        config = DebugConfig

    return config


config = load_config()

__all__ = [
    config
]
