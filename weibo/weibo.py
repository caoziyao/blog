import time

from flask import Flask
from flask import render_template
from weibo_index import main as weibo_routes





app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'r2a4n5d&o/m? /s(t)r*i&n^g@'
# ?
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
app.register_blueprint(weibo_routes)




@app.errorhandler(404)
def error404(e):
    return render_template('404.html')



if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)
