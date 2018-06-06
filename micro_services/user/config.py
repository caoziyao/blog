# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/6 
@desc:
"""


class BaseConfig:
    """基础配置"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """测试环境配置"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """生产环境配置"""
    DEBUG = False
