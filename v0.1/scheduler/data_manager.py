# coding: utf-8

import pymysql
from app.handlers import config

class DataManager(object):
    _instance = None
    _pool = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        if self._pool is None:
            cf = config.db
            self._pool = pymysql.connect(
                host=cf['host'],
                port=cf['port'],
                user=cf['username'],
                password=cf['password'],
                db=cf['dbname'],
                charset=cf['charset'],
                cursorclass=pymysql.cursors.DictCursor,
            )