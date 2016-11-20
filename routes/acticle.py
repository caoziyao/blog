from . import *


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('acticle', __name__)

@main.route('/')
def new_acticle():
    return render_template('myblog_newaticle.html')