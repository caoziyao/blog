from . import ModelHelper
from . import db
from . import timestamp
import json


# 定义一个 Model，继承自 db.Model
class BlogComment(db.Model, ModelHelper):
    __tablename__ = 'blogcomments'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer, default=0)
    comment = db.Column(db.String())

    # 定义外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))


    def __init__(self, form):
        self.created_time = timestamp()
        self.comment = form.get('comment', '')


    def json(self):
        d = {
            'comment': self.comment,
            'created_time': self.created_time,
            'username': self.username,
        }
        return json.dumps(d, ensure_ascii=False)


class Weibo_Comment(db.Model, ModelHelper):
    """
    评论微博
    """
    __tablename__ = 'weibocomments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    create_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String(), default='')

    # 定义关系
    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)

    def __init__(self, form):
        self.comment = form.get('comment', '')
        self.created_time = timestamp()
        self.username = form.get('username', '')
