#装饰器类，统计函数执行次数
class CallingParameter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0
        self.velocity = []
        self.temperature = []

    def __call__ (self, *args, **kwargs):
        self.count += 1
        self.velocity = self.velocity + [kwargs['velocity']]
        self.temperature = self.temperature + [kwargs['temperature']]
        return self.func(*args, **kwargs)

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)