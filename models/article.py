from . import ModelHelper
from . import db
from . import timestamp



# 定义一个 Model，继承自 db.Model
class Article(db.Model, ModelHelper):
    __tablename__ = 'articles'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    popular = db.Column(db.Integer, default=0)
    created_time = db.Column(db.Integer, default=0)
    content = db.Column(db.String())

    # 定义关系

    def __init__(self, form):
        self.title = form('title', '')
        self.author = 'czy'
        self.popular = 0
        self.created_time = int(time.time())
        self.content = form('content', '')