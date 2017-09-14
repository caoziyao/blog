# coding: utf-8

import os
import json

def load_file(path):
    with open(path, 'r') as f:
        data = f.read()
        s = json.loads(data, encoding='utf-8')
        return s


def read_config():
    config_path = os.path.join('config', 'config.json')
    config = load_file(config_path)

    return config