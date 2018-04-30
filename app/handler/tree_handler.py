# coding: utf-8

import os
import json
import datetime
from app.utils.const import WikiRoot, ignore_file
from .base_handler import BaseHandler
from app.model import Node, Tree

from app.dbbase import DBSession, BookModel

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
            'save_note': self.save_note,
        }
        f = tree_route.get(action, None)
        if f is not None:
            f()

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
                node = Node(data)
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
                node = Node(data)
                root.add_child(node)

    def get_tree_root(self):
        name = os.path.basename(WikiRoot)
        data = {
            'name': name,
            'isFolder': True,
            'depth': 0,
            'path': WikiRoot,
            'open': True,
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

    def save_db(self):
        pass
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

    def save_note(self):
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

