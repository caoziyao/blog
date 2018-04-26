# coding: utf-8

import os
from app.untils import load_file

class ConfigHandler(object):
    _instance = None
    _members = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.path = os.path.join('config', 'config.json')
        self.load_config()

    def load_config(self):
        """
        加载配置
        :return:
        """
        path = self.path
        self._members = load_file(path)
        return self.members


    @property
    def members(self):
        """
        取得数据字典
        :return:
        """
        return self._members


    def __getattr__(self, item):
        """
        以类属性的方式访问数据字典
        :param item:
        :return:
        """
        if item in self._members:
            return self._members[item]

        return None


config = ConfigHandler()