# coding: utf-8

import os
import json
import datetime
import tornado.web
from app.handler.base_handler import BaseHandler
from app.utils.const import WikiRoot, ignore_file
from micro_services.mznv.model import NodeModel, TreeModel, BookModel

from app.database import DBSession

class TreeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, action=''):
        name = os.path.basename(WikiRoot)
        data = {
            'name': name,
            'isFolder': True,
            'depth': 0,
            'path': WikiRoot,
            'open': True,
        }
        root = NodeModel(data)
        tree = TreeModel(root)

        self.traverse(root, WikiRoot, 0)
        d = tree.format_dict()
        self.write(json.dumps(d))


    def traverse(self, root, path, depth=0):
        for item in os.listdir(path):
            if item in ignore_file:
                continue
            child_path = os.path.join(path, item)
            if os.path.isdir(child_path):
                data = {
                    'name': item,
                    'isFolder': True,
                    'depth': depth + 1,
                    'path': child_path,
                    'open': False,
                }
                node = NodeModel(data)
                root.add_child(node)

                self.traverse(node, child_path, depth + 1)
            else:
                data = {
                    'name': item,
                    'isFolder': False,
                    'depth': depth + 1,
                    'path': child_path,
                    'open': False,
                }
                node = NodeModel(data)
                root.add_child(node)

