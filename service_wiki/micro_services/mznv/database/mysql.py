# coding: utf-8

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from micro_services.mznv.config import Config as conf

# 创建对象的基类:
# Base = declarative_base()
pymysql.install_as_MySQLdb()
Base = declarative_base()

class MySQL(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MySQL, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # ImportError: No module named 'MySQLdb'

        # 初始化数据库连接:
        engine = create_engine(conf.mysql_engine)
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=engine)

sql = MySQL()
DBSession = sql.DBSession