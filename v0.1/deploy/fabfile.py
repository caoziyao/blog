# coding:utf-8
#!/user/bin/python

import re
import sys
from time import sleep
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


def send_wiki():
    """发送代码到服务器"""
    local("rsync -vrtcp --progress --exclude '*.pyc' --delete  /Users/Shared/github/wiki root@45.76.101.36:/root")


if __name__ == '__main__':
    send_wiki()
