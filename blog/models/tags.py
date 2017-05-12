from . import ModelHelper
from . import db
from . import timestamp


# 定义一个 Model，继承自 db.Model
class Tag(db.Model, ModelHelper):
    __tablename__ = 'tags'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    tagtitle = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.tagtitle = form('tagtitle', '')
        self.created_time = timestamp()


# 定义一个 Model，继承自 db.Model
class Article_has_Tags(db.Model, ModelHelper):
    __tablename__ = 'art_tags'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer, default=0)

    # 定义外键
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))


    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    # 自动关联 不用手动查询就有数据
    tag = db.relationship('Tag', backref='arttags')
    article = db.relationship('Article', backref='arttags')

    def __init__(self):
        self.created_time = timestamp()