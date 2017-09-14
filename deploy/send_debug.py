# coding:utf-8
#!/user/bin/pythons

import re
import sys
from time import sleep

from fabric.api import settings, run, local, cd

from fabfile import sendCodeToDebugSvr


if __name__ == '__main__':
    sendCodeToDebugSvr()
