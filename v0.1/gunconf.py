# coding=utf-8
import sys
import os
import multiprocessing
# gunicorn -w4 -b0.0.0.0:3400 appcorn:application

path_of_current_file = os.path.abspath(__file__)
path_of_current_dir = os.path.split(path_of_current_file)[0]

_file_name = os.path.basename(__file__)

sys.path.insert(0, path_of_current_dir)



worker_class = 'sync'
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4

chdir = path_of_current_dir

worker_connections = 1000
timeout = 30
max_requests = 2000
graceful_timeout = 30

loglevel = 'info'

reload = True
debug = False


bind = "%s:%s" % ("0.0.0.0", 3200)
pidfile = '%s/log/run/%s.pid' % (path_of_current_dir, _file_name)
errorlog = '%s/log/%s_error.log' % (path_of_current_dir, _file_name)
accesslog = '%s/log/%s_access.log' % (path_of_current_dir, _file_name)