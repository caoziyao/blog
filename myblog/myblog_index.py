from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from models import User
# http://wdxtub.com/

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('myblog', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/')
def myblog_index():
    return render_template('myblog_index.html')


@main.route('/myblog/add')
def myblog_add():
    """
    添加博客文章
    """
    pass


@main.route('/comment/add')
def comment_add():
    """
    添加评论
    """



