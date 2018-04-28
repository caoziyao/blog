# coding: utf-8

import os
import json
from app.utils.const import WikiRoot
from .base_handler import BaseHandler
from app.model import Node, Tree

class TreeHandler(BaseHandler):
    def get(self, action=''):
        print('get action', action)
        tree_route = {
            'get_tree_root': self.get_tree_root,
        }
        f = tree_route.get(action, None)
        if f is not None:
            f()

    def post(self, action=''):
        print('post action', action)
        tree_route = {
            'load_note': self.load_note,
        }
        f = tree_route.get(action, None)
        if f is not None:
            f()

    def traverse(self, root, path, depth=0):
        for item in os.listdir(path):
            child_path = os.path.join(path, item)
            if os.path.isdir(child_path):
                data = {
                    'name': item,
                    'isFolder': True,
                    'depth': depth + 1,
                    'path': child_path,
                }
                node = Node(data)
                root.add_child(node)

                self.traverse(node, child_path, depth + 1)
            else:
                data = {
                    'name': item,
                    'isFolder': False,
                    'depth': depth + 1,
                    'path': child_path,
                }
                node = Node(data)
                root.add_child(node)

    def get_tree_root(self):
        name = os.path.basename(WikiRoot)
        data = {
            'name': name,
            'isFolder': True,
            'depth': 0,
            'path': WikiRoot,
        }
        root = Node(data)
        tree = Tree(root)

        self.traverse(root, WikiRoot, 0)
        d = tree.format_dict()
        self.write(json.dumps(d))

    def load_note(self):
        """post"""
        request_body = json.loads(self.request.body)
        path = request_body.get('path', '')
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                s = f.read()
                data = {
                    'status': 1,
                    'content': s.decode(),
                }
                self.write(json.dumps(data))
