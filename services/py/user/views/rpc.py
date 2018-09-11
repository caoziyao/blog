# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
from user.views.user import path as path_user

patchers = {}

patchers.update(path_user)

__all__ = [
    patchers,
]
