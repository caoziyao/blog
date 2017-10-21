# coding: utf-8
# from .db_manager import DBManager
from .base_model import BaseModel


class TbCatalogModel(BaseModel):

    def __init__(self):
        self.table_name = 'tb_catalog'
        super(TbCatalogModel, self).__init__(self.table_name)
        
