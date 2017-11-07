# coding: utf-8

import os
import logging
import requests
from pathlib import Path

logger = logging.getLogger('testlog')
session = requests.Session()

class Variables(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Variables, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.session = session
        self.payload = None
        self.cookies = None
        self.csrf = None

vars = Variables()





