from random import randrange


import random
from tkinter.filedialog import test

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0
        self.m = []

    def __call__ (self, *args, **kwargs):
        self.count += 1
        self.m = self.m + [kwargs['t']]
        return self.func(*args, **kwargs)

@CallingCounter
def testfun(**kwargs):
    boundaryT = kwargs['t']


for i in range(0,20):
    a = random.uniform(0,1)
    testfun(t = a)
    print(testfun.count)
    print(testfun.m)