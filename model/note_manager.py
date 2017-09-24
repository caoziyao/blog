# coding: utf-8

from database import DataManager
from .note_model import TbNoteModel
from untils import log

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
        fields = ['id', 'catalog_id', 'title', 'update_time']
        order = 'update_time desc'

        condition = {
            'catalog_id': catid
        }

        column = data_manager.fetch_rows(table, fields=fields, condition=condition, order=order)
        return column

    def total_page(self):

        sql = 'select count(`id`) as count from `tb_note`'
        data_manager = DataManager()

        r = data_manager.query(sql)

        return r[0].get('count', 1) if r else 0




    def all_notes(self, page_no):
        """
        全部笔记
        page_no: 当前页数，0-返回全部
        :return:
        """
        page_no = int(page_no)
        data_manager = DataManager()
        per_page = 20

        table = 'tb_note'
        fields = ['id', 'catalog_id', 'title', 'update_time']
        order = 'update_time desc'


        if page_no:
            start = (page_no-1) * per_page
            limit = '{},{}'.format(start, per_page)
            column = data_manager.fetch_rows(table, fields=fields, limit=limit, order=order)
        else:
            column = data_manager.fetch_rows(table, fields=fields, order=order)
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

    def get_note_content(self, note_id):
        """
        查找笔记内容
        :param parent_id:
        :return:
        """
        data_manager = DataManager()

        table = 'tb_note'
        fields = ['id', 'catalog_id', 'title', 'content']
        condition = {
            'id': note_id
        }

        column = data_manager.fetch_rows(table, fields, condition)
        return column[0]


note_manager = NoteManager()