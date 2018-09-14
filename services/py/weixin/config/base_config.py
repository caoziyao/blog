# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""

from config_default.default import EnvironmentConfig


class BaseConfig(EnvironmentConfig):

    service_name = 'srv-weixin'
    address = 'srv-weixin'
    port = 4000
