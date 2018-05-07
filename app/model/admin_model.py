# coding: utf-8

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from .base_model import BaseModel
from app.database import Base


class AdminModel(Base):
    # 表的名字:
    __tablename__ = 'ac_admin'

    # 表的结构:
    id = Column(Integer, primary_key=True, doc="主键id")
    admin_name = Column(String(255), doc='admin名称')
    password = Column(String(255), doc='密码')
    email = Column(String(255), doc='email')
    email_password = Column(String(255), doc='email_password')
    create_time = Column(DateTime, doc='创建时间')
    update_time = Column(DateTime, doc='新建时间')
