# coding: utf-8

from app.database import DataManager
from .catalog_model import TbCatalogModel

class CatalogManager():


    def __init__(self):
        pass


    def get_catalog(self):
        note = TbCatalogModel()

        note.load_members()

        return note.members


    def load_columns(self):
        """
        加载数据库
        :return:
        """
        data_manager = DataManager()
        # def fetch_rows(self, table, fields=None, condition=None, order=None, limit=None, fetchone=False):
        table = 'tb_catalog'
        fields = ['id', 'catalog_id', 'title']
        columns = data_manager.fetch_rows(table, fields)

        return columns






catalog_manager = CatalogManager()