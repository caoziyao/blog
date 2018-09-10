# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/4
@desc:
"""

from notebook.model.notebook_model import NotebookModel
from notebook.database.init_mydql import get_session


class NotebookManger(object):

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
        # if m:
        #
        #  data = m.to_json()
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

    def add_one_notebook(self, data):
        """
        单个添加
        :param data:
        :return:
        """
        session = self.session

        name = data.get('name', '')
        _id = data.get('id', '')
        update_time = data.get('update_time', '')

        if not _id:
            m = NotebookModel(id=_id, name=name, update_time=update_time)
        else:
            m = NotebookModel(name=name, update_time=update_time)
        session.merge(m)

        session.commit()

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

    # def add_notebook(self, data):
    #     """
    #
    #     :param data:
    #     :return:
    #     """
    #     session = self.session
    #
    #
    #     if isinstance(data, list):
    #         for d in data:
    #             name = d.get('name', '')
    #             m = NotebookModel(name=name)
    #             session.add(m)
    #
    #     session.commit()

    # session.add(NotebookModel)
