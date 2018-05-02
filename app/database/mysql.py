# coding: utf-8

import pymysql
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import Config as conf

# ImportError: No module named 'MySQLdb'
pymysql.install_as_MySQLdb()

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
engine = create_engine(conf.mysql_engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
