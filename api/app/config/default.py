# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

class DefaultConfig(object):
    """基础配置"""

    seconds = 30
    minute = 60
    hour = 60 * 60
    day = 24 * 60 * 60
    month = 30 * 24 * 60 * 60
    year = 365 * 24 * 60 * 60
    half_hour = 30 * 60
    half_day = 12 * 60 * 60
    half_month = 15 * 24 * 60 * 60

    max_workers = 10

    # session
    # base64.urlsafe_b64encode(os.urandom(32))
    secret = 'u95715NkcleDwO-J6P4HC_ghHbskgyZ3yVLKnQg-l1w='
    session_timeout = 2 * day

    # redis 缓存时间
    redis_cache_timeout = 5 * minute

    timeout_channel = 10
    timeout_client_side = seconds


