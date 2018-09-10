# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
from notebook.views.notebook import path as path_notebook
from notebook.views.note import path as path_note

patchers = {}

patchers.update(path_notebook)
patchers.update(path_note)

__all__ = [
    patchers,
]
