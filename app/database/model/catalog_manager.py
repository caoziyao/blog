# coding: utf-8

from .db_manager import DBManager
from .catalog_model import TbCatalogModel


class CatalogManager():

    def __init__(self):
        pass

    def catalog(self):
        """
        加载数据库
        :return:
        """
        data_manager = DBManager()
        table = 'tb_catalog'
        fields = ['id', 'title']
        columns = data_manager.fetch_rows(table, fields)

        return columns


catalog_manager = CatalogManager()
