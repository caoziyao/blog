from . import *

from models.user import User
from utils import sh1hexdigest

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('user', __name__)

def current_user():
    """
    当前用户
    session 获得 user_id
    """
    uid = session.get('user_id')
    if uid is not None:
        return User.query.get(uid)
    # else:
    #     return User.query.get(1)    # 1 代表游客


def is_superuser():
    """
    管理员用户，只有一个
    """
    u = current_user()
    if u is not None and u.username == 'root':
        return True
    else:
        return False


@main.route('/user', methods=['GET'])
def user():
    return render_template('myblog_login.html')


@main.route('/user/login', methods=['POST'])
def login():
    """
    登陆
    """
    form = request.form
    u = User(form)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    user = User.query.filter_by(username=u.username).first()
    if u.valid_login(user):
        print('登陆成功')
        session['user_id'] = user.id
        return redirect(url_for('myblog.myblog_index'))
    else:
        print('用户/密码错误')
        return render_template('myblog_login.html')


@main.route('/user/register', methods=['POST'])
def register():
    """
    注册
    """
    form = request.form
    u = User(form)
    if u.valid_register():
        print('register', form)
        u.password = sh1hexdigest(form.get('password', ''))
        u.save()
        print('注册成功')
        return redirect(url_for('user.login'))
    else:
        print('注册失败')
        return render_template('myblog_login.html')



@main.route('/logout')
def logout():
    """
    登出
    """
    session.pop('user_id', None)
    return redirect('/')