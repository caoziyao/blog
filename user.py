from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from models import User

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('user', __name__)


@main.route('/user/login', methods=['GET', 'POST'])
def login():
    """
    登陆
    """
    if request.method == 'POST':
        form = request.form
        u = User(form)
        # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
        user = User.query.filter_by(username=u.username).first()
        if u.valid_login(user):
            print('登陆成功')
            session['user_id'] = user.id
            return redirect(url_for('myblog.myblog_index'))
        else:
            print('登陆失败')
            return render_template('myblog_login.html')
    else:
        return render_template('myblog_login.html')


@main.route('/user/register', methods=['GET', 'POST'])
def register():
    """
    注册
    """
    if request.method == 'POST':
        # 注册
        form = request.form
        u = User(form)
        if u.valid_register():
            print('register', form)
            u.save()
            print('注册成功')
            return redirect(url_for('myblog.myblog_index'))
        else:
            print('注册失败')
            return render_template('myblog_login.html')
    else:
        return render_template('myblog_login.html')
