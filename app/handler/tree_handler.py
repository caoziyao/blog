# coding: utf-8

import os
import json
from app.utils.const import WikiRoot
from .base_handler import BaseHandler


class TreeHandler(BaseHandler):

    def get(self, action=''):
        print('action', action)
        tree_route = {
            'get_tree_root': self.get_tree_root
        }
        f = tree_route.get(action, None)
        if f is not None:
            f()

    def get_tree_root(self):
        root = WikiRoot

        d = {
            'path': root,
            'is_leaf': False,
        }

        self.write(json.dumps(d))
