# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

import pymysql
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# # 创建对象的基类:
pymysql.install_as_MySQLdb()
Base = declarative_base()

# 初始化mysql连接
SQL_CONFIG = {
    'pool_size': 100,
    'echo': False,
    'pool_recycle': 300,
    'convert_unicode': True
}

db_name = 'db_user'
mysql_engine = 'mysql+pymysql://root:dbjVtest#JIJ8@mysql:3306/{}?charset=utf8mb4'
mysql_engine = mysql_engine.format(db_name)

engine = create_engine(mysql_engine, **SQL_CONFIG)
DBSession = scoped_session(sessionmaker(bind=engine))


def get_session():
    s = DBSession()
    return s

# class DatabaseManger(object):
#     _instance = None
#
#     def __new__(cls, *args, **kw):
#         if not cls._instance:
#             cls._instance = super(DatabaseManger, cls).__new__(cls, *args, **kw)
#
#         return cls._instance
