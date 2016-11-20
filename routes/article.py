
from models.article import Article
from models.user import User
from models.comment import BlogComment
from routes.user import current_user
from routes.user import is_superuser

from . import *


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('article', __name__)


@main.route('/new', methods=[ 'GET', 'POST'])
def new_article():
    """
    新文章
    """
    u = current_user() 
    if request.method == 'GET':
        return render_template('myblog_newarticle.html', user=u)
    else:
        form = request.form
        title = form.get('title', '')
        content = form.get('content', '')
        a = Article(form)
        a.user_id = u.id
        a.save()
        return redirect(url_for('myblog.myblog_index'))
        # return render_template('myblog_newarticle.html', user=u)


@main.route('/<int:article_id>', methods=['GET'])
def article(article_id):
    """
    博客文章
    """
    u = current_user()  
    a = Article.query.get(article_id)
    print('acticle_id', article_id)
    return render_template('myblog_article.html', acticle=a, user=u)


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
