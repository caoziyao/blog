# coding: utf-8

from database import DataManager
from .note_model import TbNoteModel

class NoteManager():


    def __init__(self):
        pass


    def get_notes(self, catalog_id):
        """
        查找笔记
        :param parent_id:
        :return:
        """
        catid = catalog_id
        data_manager = DataManager()

        table = 'tb_note'
        fields = ['id', 'catalog_id', 'title']
        condition = {
            'catalog_id': catid
        }

        column = data_manager.fetch_rows(table, fields, condition)
        return column

    def get_catalog(self, catalog_id):
        """
        查找笔记内容
        :param parent_id:
        :return:
        """
        catid = catalog_id
        data_manager = DataManager()

        table = 'tb_note'
        fields = ['id', 'catalog_id', 'title', 'content']
        condition = {
            'catalog_id': catid
        }

        column = data_manager.fetch_rows(table, fields, condition)
        return column

    def get_note_content(self, catalog_id):
        """
        查找笔记内容
        :param parent_id:
        :return:
        """
        catid = catalog_id
        data_manager = DataManager()

        table = 'tb_note'
        fields = ['id', 'catalog_id', 'title', 'content']
        condition = {
            'catalog_id': catid
        }

        column = data_manager.fetch_rows(table, fields, condition)
        return column




note_manager = NoteManager()