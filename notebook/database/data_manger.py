# coding: utf-8

import sys
import traceback
import logging
from config import option
from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient


class DataManger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataManger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.host = option.mongodb_host
        self.port = option.mongodb_port
        self.admin = option.mongodb_admin
        self.username = option.mongodb_username
        self.passwd = option.mongodb_password
        self.db_name = option.mongodb_db_name
        self.db = self.connect_database()

    def connect_database(self):
        host = self.host
        port = self.port
        admin = self.admin
        username = self.username
        passwd = self.passwd
        db_name = self.db_name

        try:
            client = MongoClient(host, port)
            admin = client[admin]
            admin.authenticate(username, passwd)
            db = client[db_name]
            print('connect mongodb success {}:{} {}.'.format(host, port, db_name))
            return db
        except Exception as e:
            logging.error(traceback.format_exc())
            print('connect mongodb failed {}:{} {}.'.format(host, port, db_name))
            sys.exit(1)


db = DataManger().db
