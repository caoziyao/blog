# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

from .get_notebook import get_notebook
from .update_notebook import update_notebook
from .delete_notebook import delete_notebook

path = {
    'notebook.get': get_notebook,
    'notebook.update': update_notebook,
    'notebook.delete': delete_notebook,
}

__all__ = [
    path
]
