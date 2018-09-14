# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from notebook.database.notebook_manger import NotebookManger

class NotebookController(object):

    def get_notebook(self, _id):
        """

        :param _id:
        :return:
        """
        manger = NotebookManger()
        nb = manger.get_notebook(_id)

        data = {
            'id': nb.id,
            'name': nb.name,
        }

        return data

    def exit_notebook(self, _id):
        """
        是否存在 Notebook
        :param _id:
        :return:
        """
        manger = NotebookManger()
        data = manger.get_notebook(_id)
        if data:
            return True
        else:
            return False


