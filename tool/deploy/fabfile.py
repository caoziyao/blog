# coding:utf-8
#!/user/bin/python

import re
import sys
from time import sleep
from password import *
from fabric.api import settings, run, local, cd



def getPid(portNo):
    output = run("netstat -anp|grep "+ str(portNo) + "  |awk '{printf $7}'|cut -d/ -f1")
    pid = re.findall(r'\d+', output)[-1]
    return pid

def progress(percent, pcount):
    """打印进度条
    @param percent: 当前进度数
    @param pcount: 总共所需的进度
    """
    pcount = float(pcount)
    hashes = '#' * int(percent / pcount * 100)
    spaces = ' ' * (100 - len(hashes))
    sys.stdout.write("\rPercent: [%s] %0.2f%%" % (hashes + spaces, percent/pcount * 100))
    sys.stdout.flush()
    sleep(1)


def restartDebugSvr():
    """重启211测试服:切换到本目录下执行fab restartTestSvr(自动重启redis+memcache)
    """
    with settings(host_string=hosts211, password=rpwd211, user=ruser211, warn_only=True):
        run('supervisorctl stop debugsoovii')
    with settings(host_string=hosts211, password=pwd211, user=user211, warn_only=True):
        print(u"Please wait for memcache data to write the MysqlDB")
        with cd('/data/appsystems/appSvr01'):
            run('python synchrodata.py')  # 同步内存数据到mysqldb
        portList = ["6371", "11211"]  # 测试服redis端口和memcache端口
        for ca in portList:
            try:
                run('kill -9' + ' ' + getPid(ca))
            except:
                pass
        for ca in range(5):  # 防止mem未启动
            run("/home/shjd/memcached-1.4.34/bin/memcached -p 11211 -d -m 2048 -u appuser -c 256 && echo 'start memcache success'")
            if getPid(11211):
                break
            else:
                print("satrt memcached again:%s" %(4-ca))
        for ca in range(5):# 防止redis未启动
            run("/usr/local/bin/redis-server /data/appsystems/redis/conf/redis6371.conf && echo 'start redis success'")
            if getPid(6371):
                break
            else:
                print("satrt redis again:%s" %(4-ca))


    with settings(host_string=hosts211, password=rpwd211, user=ruser211, warn_only=True):
        run('supervisorctl start debugsoovii')
        print("Restart restartSvr success")


def sendCodeToDebugSvr():
    """发送代码到服务器"""
    local("rsync -vrtcp --progress --exclude '*.pyc' --delete --password-file=rsyncScode211.pass /Users/Shared/github/wiki/ root@45.76.101.36:/root/wiki/app")



def send_wiki():
    """发送代码到服务器"""
    local("rsync -vrtcp --progress --exclude '*.pyc' --delete --password-file=rsyncScode211.pass /Users/cczy/yun/wiki/ root@45.76.101.36:/root/wiki/wiki")


if __name__ == '__main__':
    sendCodeToDebugSvr()
    # send_wiki()
