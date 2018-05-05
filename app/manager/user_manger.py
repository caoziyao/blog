# coding: utf-8

import json
import hashlib
from app.model import UserModel
from app.database import DBSession
from app.cache import redis_client
from app.utils.utils import hexdigest

class UserManger(object):

    def __init__(self):
        pass

    def get_username(self, username):
        session = DBSession()

        res = session.query(UserModel).filter(
            UserModel.username == username,
        ).first()
        session.close()

        return True if res else False

    def valied_username(self, username):
        res = self.get_username(username)
        if res:
            return True
        else:
            return False

    def valied_user(self, username, password):
        res = self.get_user(username, password)
        if res:
            return True
        else:
            return False

    def get_user(self, username, password):
        r = redis_client
        session = DBSession()

        res = session.query(UserModel).filter(
            UserModel.username == username,
            UserModel.password == password
        ).first()
        session.close()

        if res:
            data = {
                'username': res.username,
                'email': res.email,
            }
            return data
        else:
            return False

    def save_user(self, username, password):
        r = redis_client
        session = DBSession()

        # 创建新User对象:
        new_user = UserModel(
            username=username,
            password=password,
        )
        session.add(new_user)
        session.commit()
        session.close()

        data = {
            'username': username,
        }
        return data



