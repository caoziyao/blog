# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/15 
@desc:
"""

from .codes import service_error_codes, system_error_codes

codes = {}
codes.update(service_error_codes)
codes.update(system_error_codes)

__all__ = [
    codes
]