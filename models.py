
import time
import json

def json_save(data, path):
    """
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    # dumps:  python ---> json
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        # log('save', path, s, data)
        f.write(s)

def json_load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        # loads: json -->  python
        return json.loads(s)


class RequestData:
    """
    保存 客户端 发过来的请求
    """
    def __init__(self):
        self.method = ''
        self.path = ''
        self.protocol = ''
        self.headers = {}
        self.body = ''

    def form(self):
        body = self.body
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = args.split('=')
            f[k] = v
        return f


request = RequestData


class Model(object):
    """
    Model 是所有 model 的基类
    @classmethod 是一个套路用法
    例如
    user = User()
    user.db_path() 返回 User.txt
    """
    @classmethod
    def db_path(cls):
        """
        cls 是类名, 谁调用的类名就是谁的
        classmethod 有一个参数是 class(这里我们用 cls 这个名字)
        所以我们可以得到 class 的名字
        """
        classname = cls.__name__
        path = 'db/{}.txt'.format(classname)
        return path


    @classmethod
    def load(cls, d):
        """
        从保存的字典中生成对象
        setattr(x, 'y', v) 相当于 x.y = v
        """
        m = cls({})
        for k, v in d.items():
            setattr(m, k, v)
        return m


    @classmethod
    def all(cls):
        """
        all 方法(类里面的函数叫方法)使用 load 函数得到所有的 models
        """
        path = cls.db_path()
        models = json_load(path)
        # 这里用了列表推导生成一个包含所有 实例 的 list
        # m 是 dict, 用 cls(m) 可以初始化一个 cls 的实例
        # 不明白就 log 大法看看这些都是啥
        ms = [cls.load(m) for m in models]



class Todo(Model):
    """
    Toto 应用
    """
    def __init__(self, form):
        # id 是独一无二的一条数据
        # 每个 model 都有自己的 id
        self.id = form.get('id', None)
        self.created_time = int(time.time())
        self.content = form.get('content', '')
        self.complete = False


