# coding: utf-8

import pymysql
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# ImportError: No module named 'MySQLdb'
pymysql.install_as_MySQLdb()

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
engine = create_engine('mysql://root:zy123456@localhost:3306/wiki?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
