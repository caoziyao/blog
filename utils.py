
import time

def log(*args, **kwargs):
    """
    调试 log 保存在文件中
    """
    t = time.time()
    form = '%Y-%m-%d %H:%M:%S'
    strtime = time.strftime(form, time.localtime())

    # 打印在终端上
    # print(strtime, *args, **kwargs)

    # 保存日志
    # 因为微软默认 GBK 格式编码，为了在 linuw mac 下不出错。
    # 使用 utf-8 编码
    str_arg = ''
    for arg in args:
        str_arg += str(arg) + ' '
    # print(str_arg)
    # strtime += '\n'
    string = strtime + '\n' + str_arg + ''.join(kwargs)
    # print(string)
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(string)
        f.write('\n')
