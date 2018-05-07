# coding: utf-8

import os
import json
import datetime
from app.utils.const import WikiRoot, ignore_file
from app.handler.base_handler import BaseHandler
from app.manager import EmailManger


class EmailHandler(BaseHandler):
    def post(self):
        request_body = json.loads(self.request.body)
        email_data = request_body.get('emailData', '')
        user_email = request_body.get('userEmail', '')

        email_manger = EmailManger()
        try:
            email_manger.send_email(email_data, user_email)
            data = {
                'msg': '发送成功',
                'emailData': email_data,
                'userEmail': user_email,
            }
        except Exception as e:
            print('e', e)
            data = {
                'msg': '发送失败',
                'emailData': email_data,
                'userEmail': user_email,
            }
        self.write(json.dumps(data))
