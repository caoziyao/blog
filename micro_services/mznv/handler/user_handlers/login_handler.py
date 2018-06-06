# coding: utf-8

import json

from app.handler.base_handler import BaseHandler
from app.manager import UserManger
from app.utils.utils import hexdigest

from micro_services.mznv.config import Config


class LoginHandler(BaseHandler):

    def get(self):
        res = {
            'code': 401,
            'msg': '登录失败'
        }

        self.write(json.dumps(res))

    def post(self):
        request_body = json.loads(self.request.body)
        username = request_body.get('username', '')
        password = request_body.get('password', '')
        password = hexdigest(password)

        manger = UserManger()
        user = manger.load_user(username, password)
        if user:
            res = {
                'res': '1',
                'msg': '登录成功'
            }
            self.current_user = user
            self.set_secure_cookie("wiki_user", str(user['id']), expires=Config.session_expires)
            # self.set_cookie("_xsrf", self.xsrf_token)
        else:
            res = {
                'res': '1',
                'msg': '登录失败'
            }

        self.write(json.dumps(res))
