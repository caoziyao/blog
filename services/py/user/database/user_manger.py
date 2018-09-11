# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from user.model.user_model import UserModel
from user.database.init_mydql import get_session
from config.log import debug_log


class UserManger(object):

    def __init__(self):
        self.session = get_session()

    def get_user(self, _id):
        """
        获取
        :param id:
        :return:
        """
        session = self.session

        m = session.query(UserModel).filter(UserModel.id == _id).first()
        return m

    def update_one_user(self, data):
        """

        :param data:
        :return:
        """
        session = self.session

        username = data.get('username', '')
        _id = data.get('id', '')
        update_time = data.get('update_time', '')

        m = UserModel
        session.query(UserModel).filter(UserModel.id == _id).update({
            m.username: username,
            m.update_time: update_time,
        })
        session.commit()
        return _id

    def add_one_user(self, data):
        """
        单个添加
        :param data:
        :return:
        """
        session = self.session

        username = data.get('username', '')
        update_time = data.get('update_time', '')

        m = UserModel(username=username, update_time=update_time)
        session.add(m)
        session.flush()
        last_id = m.id

        session.commit()
        return last_id

    def delete_mutil_user(self, user_ids):
        """
        批量删除
        :return:
        """
        session = self.session
        ids = list(map(int, user_ids))
        session.query(UserModel).filter(UserModel.id.in_(ids)).delete(synchronize_session=False)
        session.commit()

    def delete_one_user(self, user_id):
        """
        删除
        :return:
        """
        session = self.session
        _id = int(user_id)
        r = session.query(UserModel).filter(UserModel.id == _id).delete()
        session.commit()
        debug_log.info('delete_one_user')
        debug_log.info(r)
