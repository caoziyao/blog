from . import ModelHelper
from . import db
from . import timestamp

# 定义一个 Model，继承自 db.Model
class Weibo(db.Model, ModelHelper):
    __tablename__ = 'weibos'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String(), default='')

    # 定义关系
    user_id = db.Column(db.Integer)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = timestamp()
        self.username = form.get('username', '')
        self.comments = []

    def load_comments(self):
        self.comments = Weibo_Comment.query.filter_by(weibo_id=self.id).all()

