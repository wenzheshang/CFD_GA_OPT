from random import randrange
import time
from dymola.dymola_interface import DymolaInterface
import pathlib
import os


import random
from tkinter.filedialog import test

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0
        self.m = []
        self.inner = []
        self.ret = []

    def __call__ (self, *args, **kwargs):
        self.count += 1
        self.m = self.m + [kwargs['t']]
        (self.inner, self.ret) = self.func(t = 295, sm = 15)
        return self.func(*args, **kwargs)

@CallingCounter
def testfun(**kwargs):
    boundaryT = kwargs['t']
    sm = kwargs['sm']
    print('1')
    return boundaryT, sm

testfun(t = 295, sm = 15)

print(testfun.m, testfun.inner, testfun.ret)


# for i in range(0,20):
#     # a = random.uniform(0,1)
#     # testfun(t = a)
#     # print(testfun.count)
#     # print(testfun.m)
#     dymola = DymolaInterface()

#     modelicaPath = pathlib.Path(os.environ["DymolaPath"])
#     #Library import
#     dirBuilding = os.path.join(modelicaPath,"Modelica/Library/Buildings-v8.0.0/Buildings 8.0.0")
#     dirModelon = os.path.join(modelicaPath,"Modelica/Library/Modelon 2.6")
#     #open Library
#     dymola.openModel(path=os.path.join(dirBuilding, 'package.mo'))
#     dymola.openModel(path=os.path.join(dirModelon, 'package.moe'))
#     dymola.openModel('D:/Backup/Documents/Dymola/AirBraytonCycle.mo')
#     problemName = 'AirBraytonCycle.ABC_test_verify'
#     endT = 100
        
#     #第一次执行模拟时采用输入的初始变量进行初始化
#     dymola_setName = ['inlet.T','set_T.k']
#     dymola_setValue = [300, 303]
#     demo_name = 'demo_results'

#     result = dymola.simulateExtendedModel(
#         problem= problemName,
#         startTime=0,
#         stopTime=endT,
#         numberOfIntervals=0,
#         outputInterval=0.0,
#         method="Dassl",
#         tolerance=0.0001,
#         fixedstepsize=0.0,
#         resultFile=os.path.join('F:/Thinking/program/pareto_front/Workdata/Fluent_Python/2023-06-25_13-57', demo_name),
#         initialNames=dymola_setName,
#         initialValues=dymola_setValue,
#         autoLoad=True
#         )

#     time.sleep(10)

#     dymola.close()
