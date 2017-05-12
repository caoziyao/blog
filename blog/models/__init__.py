from flask_sqlalchemy import SQLAlchemy
import time
import json

db = SQLAlchemy()


def timestamp():
    """
    格式化时间
    """
    strtime =  time.strftime("%Y-%m-%d-%H-%M", time.localtime()) 
    y, m, d, h, min = strtime.split('-')
    return y + '年' + m + '月' + d + '日' + ' ' + h + ':' + min


class ModelHelper(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        # self.deleted = True
        # self.save()