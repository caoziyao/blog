# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/13 
@desc:
"""
import json
from base_common.service_code import ServiceCode

class BaseError(Exception):
    pass


class ApiException(BaseError):
    """
    """

    def __init__(self,  data='', msg='', code=ServiceCode.api_error.value):
        self.code = code
        self.msg = msg
        self.data = data
        # self.args = []

    def __str__(self):
        t = """ code: {code}, msg: {msg}
        """.format(
            code=self.code,
            msg=self.msg
        ).strip()
        return t