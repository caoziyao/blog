from . import ModelHelper
from . import db
from . import timestamp

from utils import sh1hexdigest

# 定义一个 Model，继承自 db.Model
class User(db.Model, ModelHelper):
    __tablename__ = 'users'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    # 自动关联 不用手动查询就有数据
    # 定义一遍就行，因为在 Article 已经定义过 relationship
    # articles = db.relationship('Article', backref='user')
    blogComments = db.relationship('BlogComment', backref='user')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = timestamp()

    def valid_login(self, u):
        """
        校验登陆
        """
        if u is not None:
            return u.username == self.username and u.password == sh1hexdigest(self.password)
        else:
            return False
        # return u is not None and 

    def valid_register(self):
        """
        校验注册是否满足条件
        """
        u = User.query.filter_by(username=self.username).first()
        print('register', u)
        if u is None:
            if len(self.username) < 3 or len(self.password) < 3:
                print('用户名或密码太短')
                return False
            return True 
        else:
            print('用户名已经存在')
            return False