from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from utils import log

from models import Weibo


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('weibo', __name__)


@main.route('/')
def weibo_index():
    wbs = Weibo.query.all()
    print('wbs', wbs)
    return render_template('weibo_index.html', weibos=wbs)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    print(form)
    wb = Weibo(form)
    wb.save()
    return redirect(url_for('.weibo_index'))