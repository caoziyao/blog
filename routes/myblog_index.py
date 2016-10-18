from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from models.article import Article
from models.user import User
from models.blogcomment import BlogComment


from routes.user import current_user
from routes.user import is_superuser


import json
# http://wdxtub.com/

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('myblog', __name__)




@main.route('/')
def myblog_index():
    u = current_user()  # 判断是否登陆了，没有则重定向到登陆界面
    # cs = BlogComment.query.all()    # 加载所有评论
    articles = Article.query.all()
    if is_superuser():
        print('is superuser')
    # print(cs)
    # print(type(cs))   list

    return render_template('myblog_index.html', article_list=articles, user=u)


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
