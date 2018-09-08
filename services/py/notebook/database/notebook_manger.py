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

        m = session.query(NotebookModel).filter(NotebookModel.id == _id).one()

        data = m.to_json()
        return data

    def add_notebook(self, data):
        """

        :param data:
        :return:
        """
        session = self.session


        if isinstance(data, list):
            for d in data:
                name = d.get('name', '')
                m = NotebookModel(name=name)
                session.add(m)

        session.commit()

        # session.add(NotebookModel)