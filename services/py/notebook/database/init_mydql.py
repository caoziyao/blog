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
from notebook.config import config

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

db_name = 'db_notebook'
password = config.MYSQL_ROOT_PASSWORD
mysql_engine = 'mysql+pymysql://root:{}@mysql:3306/{}?charset=utf8mb4'.format(password, db_name)

engine = create_engine(mysql_engine, **SQL_CONFIG)
DBSession = scoped_session(sessionmaker(bind=engine))


def get_session():
    s = DBSession()
    return s

