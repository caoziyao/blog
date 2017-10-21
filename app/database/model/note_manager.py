# coding: utf-8

from .db_manager import DBManager
# from app.untils import log
from .note_model import NoteModel
from .base_manager import BaseManager


class NoteManager(BaseManager):
    def __init__(self):
        pass

    def get_notes(self, catalog_id):
        """
        查找笔记
        :param parent_id:
        :return:
        """
        catid = catalog_id

        fields = ['id', 'catalog_id', 'title', 'update_time']
        order = 'update_time desc'

        condition = {
            'catalog_id': catid
        }

        note = NoteModel()
        res = note.load_data(fields=fields, condition=condition, order=order, fetchone=False)
        if res:
            rdata = note.column
        else:
            rdata = []

        return rdata

    def total_page(self):

        sql = 'select count(`id`) as count from `tb_note`'
        data_manager = DBManager()

        r = data_manager.query(sql)

        return r[0].get('count', 1) if r else 0

    def all_notes(self, page_no=0):
        """
        全部笔记
        page_no: 当前页数，0-返回全部
        :return:
        """
        page_no = int(page_no)
        per_page = 20

        fields = ['id', 'catalog_id', 'title', 'update_time']
        order = 'update_time desc'
        note = NoteModel()
        if page_no:
            start = (page_no - 1) * per_page
            limit = '{},{}'.format(start, per_page)
            res = note.load_data(fields=fields, limit=limit, order=order, fetchone=False)
        else:
            res = note.load_data(fields=fields, order=order, fetchone=False)

        if res:
            rdata = note.column
        else:
            rdata = []

        return rdata

    def get_catalog(self, catalog_id):
        """
        查找笔记内容
        :param parent_id:
        :return:
        """
        cond = {
            'catalog_id': catalog_id
        }
        fields = ['id', 'catalog_id', 'title', 'content']

        note = NoteModel()
        res = note.load_data(fields=fields, condition=cond)
        if res:
            rdata = note.column[0]
        else:
            rdata = []

        return rdata

    def get_note_content(self, note_id):
        """
        查找笔记内容
        :param parent_id:
        :return:
        """
        cond = {
            'id': note_id
        }
        fields = ['id', 'catalog_id', 'title', 'content']

        note = NoteModel()
        res = note.load_data(fields=fields, condition=cond)
        if res:
            rdata = note.column[0]
        else:
            rdata = []

        return rdata

    def update_note(self, note_id, data):
        """
        更新note
        :param note_id:
        :param data:
        :return:
        """
        condition = {
            'id': note_id
        }
        note = NoteModel()
        res = note.load_data(condition=condition)
        if res:
            note.members['views'] = data.get('views', 0)
            note.update_data()

    def views_from_db(self, note_id):
        """ 从数据库读取
        """
        condition = {
            'id': note_id
        }
        note = NoteModel()
        res = note.load_data(condition=condition)
        if res:
            views = note.views
            result = True
        else:
            result = False
            views = None

        rdata = {
            'result': result,
            'views': views,
        }
        return rdata


note_manager = NoteManager()
