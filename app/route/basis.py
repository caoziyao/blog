# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log, send_failure, send_success
# from app.database import  redis_client
from app.database import note_manager, catalog_manager
from config.constant import static_folder, template_folder

# from .hot_spot import update_views, views_from_cached


app = Blueprint('basis', __name__, static_folder=static_folder, template_folder=template_folder)


@app.route('/', methods=['GET'])
def basis_index():
    """
    页面入口
    :return:
    """
    return render_template('basis_index.html')

