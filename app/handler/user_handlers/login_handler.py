# coding: utf-8

import os
import json
import datetime
from app.handler.base_handler import BaseHandler
from app.utils.utils import hexdigest
from app.manager import UserManger

class LoginHandler(BaseHandler):
    def post(self):
        request_body = json.loads(self.request.body)
        username = request_body.get('username', '')
        password = request_body.get('password', '')
        password = hexdigest(password)

        manger = UserManger()
        data = manger.valied_user(username, password)
        if data:
            res = {
                'res': '1',
                'msg': '登录成功'
            }
        else:
            res = {
                'res': '1',
                'msg': '登录失败'
            }

        self.write(json.dumps(res))
