# api 只返回数据

from . import *

from models.user import User
from models.comment import BlogComment

import json
# http://wdxtub.com/

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('api', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u



@main.route('/comment/add', methods=['POST'])
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

