# coding: utf-8

from .db_manager import DBManager
from app.untils import log
from .note_model import NoteModel
from .base_manager import BaseManager
from app.database.cache import redis_client
from app.handlers import DatetimeHandler

class NoteManager(BaseManager):

    def __init__(self):
        """ init
        """
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
        res = note.load_data(
            fields=fields,
            condition=condition,
            order=order,
            fetchone=False,
        )
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
            res = note.load_data(
                fields=fields,
                limit=limit,
                order=order,
                fetchone=False,
            )
        else:
            res = note.load_data(fields=fields, order=order, fetchone=False)

        if res:
            rdata = note.column
            for r in rdata:
                r['update_time'] = DatetimeHandler.format_tostring(r.get('update_time', None))
        else:
            rdata = []

        return rdata

    def note_from_catalog(self, catalog_id):
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
        res = note.load_data(fields=fields, condition=cond, fetchone=False)
        if res:
            rdata = note.column
        else:
            rdata = []

        return rdata

    def note(self, note_id):
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
        res = note.load_data(fields=fields, condition=cond, fetchone=True)
        if res:
            rdata = note.column[0]
        else:
            rdata = {}

        return rdata

    def new_note(self, data):
        """
        新建 note
        :param data:
        :return: note_id
        """
        note = NoteModel()
        for k, v in data.items():
            note.members[k] = v

        result = note.add_note()

        return result, note.id


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
            for k, v in data.items():
                note.members[k] = v
            result = note.update_data()
        else:
            result = False

        return result

    def views_from_cached(self, note_id):
        """"""
        return 0


    def update_views(self, note_id):
        """
        pass
        :param note_id:
        :return:
        """
        r = redis_client
        condition = {
            'id': note_id
        }
        note = NoteModel()
        res = note.load_data(condition=condition)

        return res
        # key = 'visit:{}:totals'.format(str(note_id))
        # # 应用程序先从cache取数据，没有得到，则从数据库中取数据，成功后，放到缓存中
        # if not r.exists(key):
        #     res = note_manager.views_from_db(note_id)
        #     if res.get('result'):
        #         views = res.get('views', 0)
        #         # 设置失效时间
        #         r.set(key, views, ex=60)
        #     else:
        #         views = 0
        # else:
        #     views = r.get(key)
        # return int(views)


note_manager = NoteManager()
