from . import ModelHelper
from . import db
from . import timestamp



# 定义一个 Model，继承自 db.Model
class Article(db.Model, ModelHelper):
    __tablename__ = 'articles'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    content = db.Column(db.String())

    # 定义外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    # 自动关联 不用手动查询就有数据
    user = db.relationship('User', backref='article')
    blogComments = db.relationship('BlogComment', backref='article')

    def __init__(self, form):
        self.title = form('title', '')
        self.created_time = timestamp()
        self.content = form('content', '')