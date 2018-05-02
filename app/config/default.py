# coding: utf-8


class Config(object):

    # redis
    redis_host = 'localhost'
    redis_port = 6400
    redis_password = 'wiki@Redis'
    redis_db = 0

    # mysql
    mysql_engine = 'mysql://root:zy123456@localhost:3306/wiki?charset=utf8'
