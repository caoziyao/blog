from models.article import Article

from blog.routes import current_user
from . import *


# http://wdxtub.com/

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('myblog', __name__)


@main.route('/')
def myblog_index():
    u = current_user()  # 判断是否登陆了，没有则重定向到登陆界面
    articles = Article.query.all()

    return render_template('myblog_index.html', article_list=articles, user=u)


# @main.route('/myblog/article/add')
# def myblog_add():
#     """
#     添加博客文章
#     """
#     pass
