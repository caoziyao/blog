from . import ModelHelper
from . import db
from . import timestamp
import json


# 定义一个 Model，继承自 db.Model
class BlogComment(db.Model, ModelHelper):
    __tablename__ = 'blogcomments'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    comment = db.Column(db.String())
    replys = db.Column(db.Integer)       # 评论数

    # 定义关系
    user_id = db.Column(db.Integer)

    def __init__(self, form):
        self.username = form.get('username', '游客')
        self.created_time = timestamp()
        self.comment = form.get('comment', '')

    def json(self):
        d = {
            'comment': self.comment,
            'created_time': self.created_time,
            'username': self.username,
        }
        return json.dumps(d, ensure_ascii=False)
