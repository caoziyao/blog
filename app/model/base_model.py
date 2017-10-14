# coding: utf-8

from app.database import DataManager

class BaseModel(object):

    def __init__(self, table_name):
        self._table_name = table_name
        self._members = {}
        self._column = []

        self.load_members()

    def load_members(self):
        """
        加载数据库字段
        :return:
        """
        manager = DataManager()
        table_name = self._table_name
        sql = 'SHOW COLUMNS FROM {}'.format(table_name)

        columns = manager.query(sql)
        for col in columns:
            field = col['Field']
            default = col['Default']
            self._members[field] = default


    @property
    def column(self):
        """
        取得数据列表
        :return:
        """
        return self._column

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


