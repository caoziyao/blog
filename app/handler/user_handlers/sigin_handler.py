# coding: utf-8

import os
import json
import datetime
from app.utils.const import WikiRoot, ignore_file
from app.handler.base_handler import BaseHandler

from app.manager import UserManger
from app.utils.utils import hexdigest

class SiginHandler(BaseHandler):
    def post(self):
        request_body = json.loads(self.request.body)
        username = request_body.get('username', '')
        password = request_body.get('password', '')
        password = hexdigest(password)

        manger = UserManger()
        data = manger.valied_username(username)
        if data:
            res = {
                'res': '1',
                'msg': '已经注册改用户名'
            }
        else:
            res = manger.save_user(username, password)
        self.write(json.dumps(res))
