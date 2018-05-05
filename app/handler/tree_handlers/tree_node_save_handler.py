# coding: utf-8

import os
import json
import datetime
from app.handler.base_handler import BaseHandler
from app.utils.const import WikiRoot, ignore_file
from app.model import NodeModel, TreeModel, BookModel

from app.database import DBSession


class TreeNodeSaveHandler(BaseHandler):
    def post(self, action=''):
        """post"""
        request_body = json.loads(self.request.body)
        path = request_body.get('path', '')
        value = request_body.get('value', '').encode()
        if os.path.isfile(path):
            with open(path, 'wb') as f:
                f.write(value)
                data = {
                    'status': 1,
                }
                self.write(json.dumps(data))

    def save_db(self):
        # 创建session对象:
        session = DBSession()
        # 创建新User对象:
        now = datetime.datetime.now()
        now = datetime.datetime.now()
        new_user = BookModel(name='Bob', create_time=now, update_time=now)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()
