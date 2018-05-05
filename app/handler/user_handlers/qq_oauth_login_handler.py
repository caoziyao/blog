# coding: utf-8

import os
import json
import time
import datetime
import tornado.auth
from app.handler.base_handler import BaseHandler
from app.utils.utils import hexdigest
from app.manager import UserManger
from app.config import Config

class GoogleOAuth2LoginHandler(tornado.auth.GoogleOAuth2Mixin, BaseHandler):

    # def get(self):
    #     res = {
    #         'code': 401,
    #         'msg': '登录失败'
    #     }
    #
    #     self.write(json.dumps(res))

    def get(self):
        if self.get_argument('code', False):
            user = self.get_authenticated_user(
                redirect_uri='http://your.site.com/auth/google',
                code=self.get_argument('code'))
            # Save the user with e.g. set_secure_cookie
        else:
            self.authorize_redirect(
                redirect_uri='http://your.site.com/auth/google',
                client_id=self.settings['google_oauth']['key'],
                scope=['profile', 'email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})
