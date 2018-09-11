# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from user.database.user_manger import UserManger

class UserController(object):

    def get_user(self, _id):
        """

        :param _id:
        :return:
        """
        manger = UserManger()
        user = manger.get_user(_id)

        data = {
            'id': user.id,
            'username': user.username,
        }

        return data

    def exit_user(self, _id):
        """
        是否存在
        :param _id:
        :return:
        """
        manger = UserManger()
        data = manger.get_user(_id)
        if data:
            return True
        else:
            return False