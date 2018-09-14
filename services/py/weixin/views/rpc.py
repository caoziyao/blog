# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
from weixin.views.weixin import path as path_weixin

patchers = {}

patchers.update(path_weixin)

__all__ = [
    patchers,
]
