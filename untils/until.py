# coding: utf-8

import os
import json
import datetime

def log(*args, **kwargs):

    now = datetime.datetime.now()
    str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(str, *args, **kwargs)

def load_file(path):
    with open(path, 'r') as f:
        data = f.read()
        s = json.loads(data, encoding='utf-8')
        return s


def read_config():
    config_path = os.path.join('config', 'config.json')
    config = load_file(config_path)

    return config