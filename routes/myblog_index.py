from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from models.user import User
from models.blogcomment import BlogComment

import json
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
    u = current_user()  # 判断是否登陆了，没有则重定向到登陆界面
    if u is None:
        return redirect('/user/register')
    cs = BlogComment.query.all()    # 加载所有评论
    # print(cs)
    return render_template('myblog_index.html', comments=cs)


# @main.route('/myblog/article/add')
# def myblog_add():
#     """
#     添加博客文章
#     """
#     pass


@main.route('/p=<article_id>')
def myblog_article(article_id):
    return render_template('myblog_article.html')


@main.route('/myblog/comment/add', methods=['POST'])
def comment_add():
    """
    添加评论
    """
    form = request.form
    print('comment', form)
    u = current_user()

    c = BlogComment(form)
    c.save()
    return c.json()
