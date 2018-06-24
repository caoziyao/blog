# coding: utf-8

import time

class Config(object):

    # redis
    redis_host = 'localhost'
    redis_port = 6400
    redis_password = 'wiki@Redis'
    redis_db = 0

    # mysql
    mysql_engine = 'mysql://root:zy123456@localhost:3306/wiki?charset=utf8'

    # session
    # session_expires_min = 15
    # session_expires = time.time() + session_expires_min * 60
    session_expires = None

    # 分类接口service层缓存时间 秒
    minute = 60
    redis_cache_time = 1 * minute
