# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from .get_note import get_note
from .update_note import update_note
from .delete_note import delete_note

path = {
    'note.get': get_note,
    'note.update': update_note,
    'note.delete': delete_note,
}

__all__ = [
    path
]
