from . import ModelHelper
from . import db
from . import timestamp


# 定义一个 Model，继承自 db.Model
class User(db.Model, ModelHelper):
    __tablename__ = 'users'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    # 定义关系

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def valid_login(self, u):
        """
        校验登陆
        """
        return u is not None and u.username == self.username and u.password == self.password

    def valid_register(self):
        """
        校验注册是否满足条件
        """
        return len(self.username) > 2 and len(self.password) > 2