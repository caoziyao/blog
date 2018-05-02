# coding: utf-8

import os
import json
import datetime
from app.handler.base_handler import BaseHandler
class TreeNodeLoadHandler(BaseHandler):


    def post(self, action=''):
        """post"""
        request_body = json.loads(self.request.body)
        path = request_body.get('path', '')
        filename = os.path.basename(path)
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                s = f.read()
                data = {
                    'status': 1,
                    'content': s.decode(),
                    'path': path,
                    'filename': filename,
                }
                self.write(json.dumps(data))



