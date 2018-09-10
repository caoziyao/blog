# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from notebook.database.note_manger import NoteManger

class NoteController(object):

    def get_note(self, _id):
        """

        :param _id:
        :return:
        """
        manger = NoteManger()
        data = manger.get_note(_id)

        return data

    def exit_note(self, _id):
        """
        是否存在
        :param _id:
        :return:
        """
        manger = NoteManger()
        data = manger.get_note(_id)
        if data:
            return True
        else:
            return False