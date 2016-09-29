from . import ModelHelper
from . import db
from . import timestamp


class Weibo_Comment(db.Model, ModelHelper):
    """
    评论微博
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    create_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String(), default='')

    # 定义关系
    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)

    def __init__(self, form):
        self.comment = form.get('comment', '')
        self.created_time = int(time.time())
        self.username = form.get('username', '')
