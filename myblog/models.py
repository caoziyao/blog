from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time
import json


# 以下都是套路
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 指定数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'

db = SQLAlchemy(app)


class ModelHelper(object):
    """
    Model 基类
    """
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


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




def init_db():
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')


if __name__ == '__main__':
    init_db()
    # """
    # select * from users where id=1
    #
    # update users set password='pwd' where id=1
    #
    # SELECT
    #     todos.id AS todos_id,
    #     todos.task AS todos_task,
    #     todos.created_time AS todos_created_time,
    #     todos.user_id AS todos_user_id
    # FROM
    #     todos
    # WHERE
    #     todos.user_id = :user_id_1
    # """
    # u = User.query.get(1)
    # # u.password = 'pwd'
    # # u.save()
    # print('sql', Todo.query.filter_by(user_id=u.id))
    # ts = Todo.query.filter_by(user_id=u.id).all()
    # print('todos', ts)