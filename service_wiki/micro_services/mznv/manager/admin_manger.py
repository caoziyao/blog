# coding: utf-8

import json
import hashlib
from micro_services.mznv.model import AdminModel
from app.database import DBSession
from app.cache import redis_client
from app.utils.utils import hexdigest


class AdminManger(object):
    def __init__(self):
        self.admin_name = 'admin'

    def get_email(self):
        data = self.load_admin()
        r = {}
        if data:
            r['email'] = data.get('email', '')
            r['email_password'] = data.get('email_password', '')
        else:
            pass

        return r

    def load_admin(self):
        r = redis_client
        session = DBSession()
        admin_name = self.admin_name

        res = session.query(AdminModel).filter(
            AdminModel.admin_name == admin_name,
        ).first()
        session.close()

        if res:
            data = {
                'username': res.admin_name,
                'id': res.id,
                'email': res.email,
                'email_password': res.email_password,
            }
            return data
        else:
            return False
