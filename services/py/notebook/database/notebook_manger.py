# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/4
@desc:
"""
from .base_manager import BaseManager
from notebook.model.notebook_model import NotebookModel
from notebook.database.init_mydql import get_session


class NotebookManger(BaseManager):

    def __init__(self):
        self.session = get_session()

    def test_demo(self):
        session = self.session
        book = NotebookModel(name='dssdfdd')

        session.add(book)
        session.commit()

    def get_notebook(self, _id):
        """
        获取 notebook
        :param id:
        :return:
        """
        session = self.session

        m = session.query(NotebookModel).filter(NotebookModel.id == _id).first()
        return m

    def get_notebooks(self, _ids):
        """
        获取 notebook
        :param id:
        :return:
        """
        session = self.session
        # _ids = list()
        m = session.query(NotebookModel).filter(NotebookModel.id.in_(_ids)).all()
        return m

    def add_mutil_notebook(self, data):
        """
        批量添加
        :return:
        """
        session = self.session
        for d in data:
            name = d.get('name', '')
            _id = d.get('id', '')
            update_time = d.get('update_time', '')
            if not _id:
                m = NotebookModel(name=name, update_time=update_time)
            else:
                m = NotebookModel(id=_id, name=name, update_time=update_time)
            session.merge(m)
        session.commit()

    def update_one_notebook(self, data):
        """

        :param data:
        :return:
        """
        session = self.session

        name = data.get('name', '')
        _id = data.get('id', '')
        update_time = data.get('update_time', '')

        m = NotebookModel
        session.query(m).filter(m.id == _id).update({
            m.name: name,
            m.update_time: update_time,
        })
        session.commit()
        return _id

    def add_one_notebook(self, data):
        """
        单个添加
        :param data:
        :return:
        """
        session = self.session

        name = data.get('name', '')
        update_time = data.get('update_time', '')

        m = NotebookModel(name=name, update_time=update_time)
        session.add(m)
        session.flush()
        last_id = m.id

        session.commit()
        return last_id

    def delete_mutil_notebook(self, notebook_ids):
        """
        批量删除
        :return:
        """
        session = self.session
        ids = list(map(int, notebook_ids))
        session.query(NotebookModel).filter(NotebookModel.id.in_(ids)).delete(synchronize_session=False)
        session.commit()

    def delete_one_notebook(self, notebook_id):
        """
        删除
        :return:
        """
        session = self.session
        _id = int(notebook_id)
        session.query(NotebookModel).filter(NotebookModel.id == _id).delete()
        session.commit()
