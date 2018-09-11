# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from .get_user import get_user
from .update_user import update_user
from .delete_user import delete_user

path = {
    'user.get': get_user,
    'user.update': update_user,
    'user.delete': delete_user,
}

__all__ = [
    path
]
