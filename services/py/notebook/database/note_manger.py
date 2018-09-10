# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from notebook.model.note_model import NoteModel
from notebook.database.init_mydql import get_session
from config.log import debug_log


class NoteManger(object):

    def __init__(self):
        self.session = get_session()

    def get_note(self, _id):
        """
        获取 notebook
        :param id:
        :return:
        """
        session = self.session

        m = session.query(NoteModel).filter(NoteModel.id == _id).first()
        return m

    def add_mutil_note(self, data):
        """
        批量添加
        :return:
        """
        session = self.session
        for d in data:
            name = d.get('name', '')
            _id = d.get('id', '')
            update_time = d.get('update_time', '')
            notebook_id = d.get('notebook_id', '')
            if not _id:
                m = NoteModel(name=name, update_time=update_time, notebook_id=notebook_id)
            else:
                m = NoteModel(id=_id, name=name, update_time=update_time, notebook_id=notebook_id)
            session.merge(m)
        session.commit()

    def update_one_note(self, data):
        """

        :param data:
        :return:
        """
        session = self.session

        name = data.get('name', '')
        _id = data.get('id', '')
        update_time = data.get('update_time', '')
        notebook_id = data.get('notebook_id', '')
        content = data.get('content', '')

        m = NoteModel
        session.query(NoteModel).filter(NoteModel.id == _id).update({
            m.name: name,
            m.update_time: update_time,
            m.notebook_id: notebook_id,
            m.content: content
        })
        session.commit()
        return _id

    def add_one_note(self, data):
        """
        单个添加
        :param data:
        :return:
        """
        session = self.session

        name = data.get('name', '')
        _id = data.get('id', '')
        update_time = data.get('update_time', '')
        notebook_id = data.get('notebook_id', '')
        content = data.get('content', '')

        m = NoteModel(name=name, update_time=update_time, notebook_id=notebook_id, content=content)
        session.add(m)
        session.flush()
        last_id = m.id

        session.commit()
        return last_id

    def delete_mutil_note(self, note_ids):
        """
        批量删除
        :return:
        """
        session = self.session
        ids = list(map(int, note_ids))
        session.query(NoteModel).filter(NoteModel.id.in_(ids)).delete(synchronize_session=False)
        session.commit()

    def delete_one_note(self, note_id):
        """
        删除
        :return:
        """
        session = self.session
        _id = int(note_id)
        session.query(NoteModel).filter(NoteModel.id == _id).delete()
