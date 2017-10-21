# coding: utf-8

from .db_manager import DBManager
# from app.untils import log


class BaseManager():

    def __init__(self, table_name):
        self._table_name = table_name
        self._manager = DBManager()
