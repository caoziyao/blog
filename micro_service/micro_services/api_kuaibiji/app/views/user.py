# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
from flask import request, session, current_app, abort
# from flask_login import current_user, login_user, logout_user, AnonymousUserMixin, UserMixin
from flask import Blueprint, render_template
import json
from rpc.notebook import NoteBookClient
from rpc.user import UserClient
import functools
from common.request_tool import send_failure, send_success
from database import redis_client
# import

mod = Blueprint('user', __name__)

def unauthorized():
    # abort(401)
    return send_failure(msg='please login in')

def login_required(func):
    """
    登陆装饰器，func的执行必须是已登陆用户，否则跳转到登陆页面
    :param func: 被装饰的函数
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # user_info = get_user_info(self.token_cache_id)
        token = 'jwmi hello ranndeeerom id'
        user_info = redis_client.get_bylock(token)
        if user_info is None:
            return unauthorized()
            # raise HTTPError(401)
        # elif user_info and toint(user_info.get('member_id', 0)) <= 0:
        #     raise HTTPError(401)
        # 将用户信息赋给view类
        # self.user_info = user_info
        return func(*args, **kwargs)

    return wrapper


# def login_required(view):
#     """View decorator that redirects anonymous users to the login page."""
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         user = current_user
#         if user.is_authenticated():
#             return send_failure(msg='not login')
#
#         return view(**kwargs)
#
#     return wrapped_view
#
# def login_user(user, remember=False, force=False, fresh=True):
#     if not force and not user.is_active:
#         return False
#
#     user_id = getattr(user, current_app.login_manager.id_attribute)()
#     session['user_id'] = user_id
#     session['_fresh'] = fresh
#     session['_id'] = current_app.login_manager._session_identifier_generator()
#
#     if remember:
#         session['remember'] = 'set'
#
#     _request_ctx_stack.top.user = user
#     user_logged_in.send(current_app._get_current_object(), user=_get_user())
#     return True

# class UserAnonymous(AnonymousUserMixin):
#
#     def __init__(self):
#         self.username = 'Guest'
#
# class User(UserMixin):
#
#     def __init__(self, user_id):
#         super(User, self).__init__()
#         self.id = user_id
#
#     def get_id(self):
#
#         return '87666'


@mod.route('/user_info')
# @login_required
def get_user():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    # user_id = args.get('user_id', '')
    s = UserClient()
    user = s.user_by_id('33')
    # user_data = user.get('data', '')
    # a = current_user.id
    # print('a', a)
    a = 'aaaaa'
    user_data = 1
    if user_data:
        return send_success(msg=a)
    else:
        return send_failure(msg=a)


@mod.route('/login')
def login():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    code = args.get('code', '')
    session.clear()
    # WeixinService().weixin_login(code)
    # session['user_id'] = 'adbd'

    # username and password yes
    username = 'abc'
    token = 'jwmi hello ranndeeerom id'
    data = {
        'token': token,
        'username': username,
    }
    redis_client.set_bylock(token, json.dumps(data), expire_time=1*60)

    # user = User('adbd')

    # login_user(user, remember=True)

    return send_success(msg='login ok')
    # s = UserClient()
    # user = s.user_by_id(user_id)
    # user_data = user.get('data', '')
    # if not user_data:
    #     return send_failure(msg='no user')


@mod.route('/logout')
def logout():
    # session.clear()
    # logout_user()
    token = 'jwmi hello ranndeeerom id'
    redis_client.delete(token)
    return send_failure(msg='no user')
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    # args = request.args
    # user_id = args.get('user_id', '')
    # s = UserClient()
    # user = s.user_by_id(user_id)
    # user_data = user.get('data', '')
    # if not user_data:
    #     return send_failure(msg='no user')
