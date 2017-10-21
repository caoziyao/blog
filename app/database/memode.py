# coding: utf-8


class MAdmin(object):

    def __init__(self, table_name):
        """
        :param table_name:
        """
        self._table_name = table_name


class MAdminManager(object):

    def __init__(self):
        pass

    def regist(self, db):

        self.db = db


tb_note = MAdmin('tb_note')
MAdminManager().registe(tb_note)
