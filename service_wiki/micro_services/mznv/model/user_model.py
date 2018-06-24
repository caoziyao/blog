# coding: utf-8

from sqlalchemy import Column, String, DateTime, Integer

# from .base_model import BaseModel
from app.database import Base

class UserModel(Base):
    # 表的名字:
    __tablename__ = 'tb_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, doc="主键id")
    username = Column(String(255), doc='username')
    email = Column(String(255), doc='email')
    password = Column(String(255), doc='password')
    update_time = Column(DateTime, doc='更新时间')
    create_time = Column(DateTime, doc='创建时间')

    def to_json(self):

        d = {
            'id': self.id,
            'name': self.username,
        }
        return d