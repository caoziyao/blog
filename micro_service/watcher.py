# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc:
"""
import os
import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

# cmd_test = ['python3', 'api_test.py']
cmd_list = [
    ['python3', 'main.py'],
    ['python3', 'api_test.py'],
]
process_list = []

def kill_process():
    # global process
    for process in process_list:
        process.kill()
        process.wait()
        # process = None


def start_process():
    # global process
    for cmd in cmd_list:
        process = subprocess.Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        process_list.append(process)


def restart_process(path):
    suffix = path.split('.')[-1]
    if suffix == 'py':
        print('watcher on_created', path)
        kill_process()
        start_process()


# 自定义事件处理类
class watcher(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        FileSystemEventHandler.__init__(self, *args, **kwargs)
        print('watcher init', *args, **kwargs)

    # def on_any_event(self, event):
    #     print('watcher on_any_event',)

    # def on_modified(self, event):
    #     path = event.src_path
    #     print('watcher on_modified ', path)
    #     restart_process(path)
        # auto_test(event.src_path)

    # def on_moved(self, event):
    #     print('watcher on_moved',)

    # def on_deleted(self, event):
    #     print('watcher on_deleted',)

    def on_created(self, event):
        path = event.src_path
        restart_process(path)


def main():
    config = dict(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logging.basicConfig(**config)
    event_handler = watcher()
    observer = Observer()
    path = '.'
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    start_process()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
