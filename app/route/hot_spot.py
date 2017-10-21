# coding: utf-8

import json
# import os
from flask import request
from flask.blueprints import Blueprint
from app.untils import log
from app.database import note_manager, redis_client
from config.constant import static_folder, template_folder
# from app.scheduler import Scheduler

app = Blueprint(
    'hot_spot',
    __name__,
    static_folder=static_folder,
    template_folder=template_folder,
)


class RWThroughPattern(object):
    """ ReadThrough / WriteThrough
    """
    def __init__(self):
        self.redis = redis_client
        # 超时过期时间，单位 s
        self.ex_time = 60

    def data_from_db(self):
        pass

    def set_cached(self):
        pass

    def data_from_cached(self, key):
        """ pass
        """
        r = redis_client
        if not r.exists(key):
            return None
        else:
            return r.get(ley)

    def views_from_cached(self, note_id, key):
        """ read
        key 格式

        """
        r = redis_client
        data = self.data_from_cached(key)
        if data is None:
            r = self.data_from_db()
            if r:
                self.set_cached()
            else:
                return None
        return data


    def write(self, note_id):
        """

        :return:
        """
        r = self.redis
        key = 'visit:{}:totals'.format(str(note_id))
        views = views_from_cached(note_id) + 1
        data = {
            'views': views,
        }
        note_manager.update_note(note_id, data)
        # 让缓存失效。
        r.delete(key)


# redis 计数
def views_from_cached(note_id):
    """
    初始点击数
    :return:
    """
    r = redis_client
    key = 'visit:{}:totals'.format(str(note_id))
    # 应用程序先从cache取数据，没有得到，则从数据库中取数据，成功后，放到缓存中
    if not r.exists(key):
        # r.set(key, 65536)
        res = note_manager.views_from_db(note_id)
        if res.get('result'):
            views = res.get('views', 0)
            # 设置失效时间
            r.set(key, views, ex=60)
        else:
            views = 0
    else:
        views = r.get(key)
    return int(views)


def update_views(note_id):
    """
    点击数
    :return:
    """
    # 更新：先把数据存到数据库中，成功后，再让缓存失效。
    r = redis_client
    key = 'visit:{}:totals'.format(str(note_id))
    views = views_from_cached(note_id) + 1
    data = {
        'views': views,
    }
    note_manager.update_note(note_id, data)
    # 让缓存失效。
    r.delete(key)
    return views


@app.route('/incr_click_number', methods=['POST'])
def incr_click_number():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    note_id = data.get('note_id', 0)
    n = update_views(note_id)

    rdata = {
        'number': n,
    }
    log('number', rdata)

    return json.dumps(rdata)
