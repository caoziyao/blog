from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from models import Weibo
from models import Weibo_Comment


import json
# http://wdxtub.com/

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是 ??
main = Blueprint('weibo', __name__)

@main.route('/weibo')
def weibo_index():
    wbs = Weibo.query.all()
    # wcs = Weibo_Comment.query.all()
    for wb in wbs:
        wb.load_comments()
    print('wbs', wbs)
    return render_template('weibo_index.html', weibos=wbs)


@main.route('/weibo/add', methods=['POST'])
def add():
    """
    添加微博
    """
    form = request.form
    print(form)
    wb = Weibo(form)
    wb.save()
    return redirect(url_for('.weibo_index'))


@main.route('/weibo/delete/<int:weibo_id>')
def delete(weibo_id):
    # 获取 微博
    wb = Weibo.query.get(weibo_id)
    # 获取 微博评论
    wcs = Weibo_Comment.query.filter_by(weibo_id=wb.id).all()

    # 删除
    wb.delete()
    for wc in wcs:
        wc.delete()
    return redirect(url_for('.weibo_index'))



@main.route('/weibo/comment/add', methods=['POST'])
def comment_add():
    """
    评论微博
    """
    form = request.form
    print('comments form', form)
    wc = Weibo_Comment(form)
    wc.weibo_id = int(form.get('weibo_id', -1))
    wc.save()
    return redirect(url_for('.weibo_index'))