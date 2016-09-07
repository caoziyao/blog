import time


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    # 中文 windows 平台默认打开的文件编码是 gbk 所以需要指定一下
    with open('log.txt', 'a', encoding='utf-8') as f:
        # 通过 file 参数可以把输出写入到文件 f 中
        # 需要注意的是 **kwargs 必须是最后一个参数
        print(dt, *args, file=f, **kwargs)
        # f.write(dt)


# def log(*args, **kwargs):
#     """
#     调试 log 保存在文件中
#     """
#     t = time.time()
#     form = '%Y-%m-%d %H:%M:%S'
#     strtime = time.strftime(form, time.localtime())
#
#     # 打印在终端上
#     # print(strtime, *args, **kwargs)
#
#     # 保存日志
#     # 因为微软默认 GBK 格式编码，为了在 linuw mac 下不出错。
#     # 使用 utf-8 编码
#     str_arg = ''
#     for arg in args:
#         str_arg += str(arg) + ' '
#     # print(str_arg)
#     # strtime += '\n'
#     string = strtime + '\n' + str_arg + ''.join(kwargs)
#     # print(string)
#     with open('log.txt', 'a+', encoding='utf-8') as f:
#         f.write(string)
#         f.write('\n')