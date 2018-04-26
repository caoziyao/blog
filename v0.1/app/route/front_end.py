# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log, send_failure, send_success
# from app.database import  redis_client
from app.database import note_manager, catalog_manager
from config.constant import static_folder, template_folder


app = Blueprint('font_end', __name__, static_folder=static_folder, template_folder=template_folder)


@app.route('/', methods=['GET'])
def font_end():
    """
    页面入口
    :return:
    """
    return render_template('font_end.html')