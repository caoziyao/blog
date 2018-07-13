# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/13
@desc:
"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from .base_model import BaseModel
from database import Base


class NotebookModel(Base):
    __tablename__ = 'tb_notebook'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    update_time = Column(DateTime, default=datetime.utcnow)
    create_time = Column(DateTime, default=datetime.utcnow)

# session = MySQLManger().session()
# # 创建新User对象:
#
# user = session.query(Notebook).filter(Notebook.id == 1).all()
# new_user = Notebook(name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
#
# # 创建Session:
# s = MySQLManger().session()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = s.query(Notebook).all()
# # 打印类型和对象的name属性:
# print(user)
