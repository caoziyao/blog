# coding: utf-8

from time import sleep
from fabric.api import settings, run, local, cd
# from batchtask import DataManager



def backup_to_file():
    """
    备份数据库到文件
    :return:
    """
    cmd = 'mysqldump -uroot -pzy123456 wiki > ../media/sql/wiki.sql'
    local(cmd)


if __name__ == '__main__':
    backup_to_file()