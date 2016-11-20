from flask import Flask, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from routes.article import main as article_routes
from routes.api import main as api_routes
from routes.myblog_index import main as myblog_routes
from routes.user import main as user_routes

# from weibo.weibo_index import main as weibo_routes


app = Flask(__name__)

db_path = 'myblog.sqlite'
manager = Manager(app)



def register_route(app):
	"""
	蓝图注册
	"""
	# url_prefix='/node'
	# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
	app.register_blueprint(myblog_routes)
	app.register_blueprint(user_routes)
	app.register_blueprint(article_routes, url_prefix='/acticle')
	app.register_blueprint(api_routes, url_prefix='/api')
	# app.register_blueprint(weibo_routes)


def configure_app():
	"""
	套路
	"""
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	# 设置 secret_key 来使用 flask 自带的 session
	# 这个字符串随便你设置什么内容都可以
	app.secret_key = 'secret key'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
	db.init_app(app)
	# 蓝图注册
	register_route(app)
	# 创建数据库
	# create_all()



def configure_manager():
	"""
	这个函数用来配置命令行选项
	"""
	# 数据库迁移
	Migrate(app, db)
	manager.add_command('db', MigrateCommand)



@app.errorhandler(404)
def error404(e):
	"""
	自定义 404 界面
	"""
	return render_template('404.html')


# 使用的时候, 初始化数据库用
# python app.py db init

# 数据改动后, 使用下面两个命令迁移并且升级数据库
# python app.py db migrate
# python app.py db upgrade

# 自定义的命令行命令用来运行服务器
@manager.command
def server():
	print('server run')
	config = dict(
		debug=True,
		host='0.0.0.0',
		port=80,
	)
	app.run(**config)


if __name__ == '__main__':
	configure_manager()
	configure_app()
	manager.run()       # 命令行

# if __name__ == '__main__':
#     config = dict(
#         debug=True,
#         host='0.0.0.0',
#         port=80,
#     )
#     app.run(**config)
