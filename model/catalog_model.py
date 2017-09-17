# coding: utf-8

from database import data_manager
from .base_model import BaseModel

class TbCatalogModel(BaseModel):


    def __init__(self):
        self.table_name = 'tb_catalog'
        super(TbCatalogModel, self).__init__(self.table_name)








