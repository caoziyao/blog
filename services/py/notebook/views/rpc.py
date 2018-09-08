# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

from jsonrpc import dispatcher
from notebook.views.notebook import path as path_notebook

patchers = {}

patchers.update(path_notebook)

__all__ = [
    patchers,
]
