# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""

from enum import Enum, unique

weixin_secret = '129617ac6483f401faad38baa641580d'
weixin_appid = 'wx871ca01ead43431b'
weixin_oauth_url = 'https://api.weixin.qq.com/sns/jscode2session'

@unique
class ResultCode(Enum):
    failure = 999
    success = 0