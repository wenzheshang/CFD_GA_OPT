from doctest import master
from subprocess import run
import random
import numpy
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

from fluent_corba import CORBA
import string
import time
import pathlib
import os, sys
import subprocess

#r = {'rank': 0} #记录优化次数

#装饰器类，统计函数执行次数
class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

#可传参的调用脚本进行后处理的批处理
def paraview_post_bat(save_path, open_path, **kwargs):

    pvpythonPath = "F:/paraview/ParaView-5.9.1-Windows-Python3.8-msvc2017-64bit/ParaView-5.9.1-Windows-Python3.8-msvc2017-64bit/bin/pvpython.exe"
    scriptPath = "F:/Thinking/program/pareto_front/view_sc.py"
    dic = kwargs
    name = ''
    for n in dic:
        name  = name + str(dic[n]).ljust(len(dic[n])+1)
    save = str(save_path)
    open = str(open_path)

    run(f'{pvpythonPath} {scriptPath} {save} {open} {name}', shell=True)

    return 

@CallingCounter
def CFD_simu(**kwargs):
    
    #r['rank'] = r['rank'] + 1

    BoundaryV = kwargs['velocity']
    BoundaryT = kwargs['temperature']
    #rank = r['rank']

    scheme.doMenuCommand('define/models/dpm/interaction/coupled-calculations? no')

    scheme.doMenuCommand('/define/boundary/velocity-inlet/inlet no no yes yes no '+str(BoundaryV)+' no 0 no 293.15 no no yes 5 10')
    scheme.doMenuCommand("/define/boundary/zone-type outlet outflow")
    
    for BoundaryName in ['ew','ww','sw','nw','uw']:
        scheme.doMenuCommand('/define/boundary/wall '+BoundaryName+' 0 no 0 no yes temperature no '+str(BoundaryT)
                              +' no no no no 0 no 0.5 no polynomial 1 1 polynomial 1 1 no 1')
    for boxname in ['eb','wb','sb','nb','ub','dw']:
        scheme.doMenuCommand('/define/boundary/wall '+boxname+' 0 no 0 no yes temperature no '+str(303.15)
                              +' no no no no 0 no 0.5 no polynomial 1 1 polynomial 1 1 no 1')

    scheme.doMenuCommand('/solve/set/p-v-coupling 20') #SIMPLE
    scheme.doMenuCommand('solve/set/discretization-scheme/pressure 14') #PRESTO!
    scheme.doMenuCommand('solve/set/discretization-scheme/mom 1') #SOU
    scheme.doMenuCommand('solve/set/discretization-scheme/k 1') #SOU
    scheme.doMenuCommand('solve/set/discretization-scheme/epsilon 1') #SOU
    scheme.doMenuCommand('solve/set/under-relaxation/k 0.7') #Relaxtion
    scheme.doMenuCommand('solve/set/under-relaxation/epsilon 0.7') #Relaxtion
    scheme.doMenuCommand('/solve/initialize/set-hyb-initialization/general-settings 30 1 1 relative no no no')
    if CFD_simu.count == 1:
        scheme.doMenuCommand("/solve/initialize/compute-defaults/all-zones")
    else:
        scheme.doMenuCommand('/solve/initialize/hyb-initialization o')
    fluentUnit.setNrIterations(500)
    fluentUnit.calculate() 
 #dpm应该在计算结束后再加入，可以减少计算时间
 ####################################################################################################################
    scheme.doMenuCommand('define/models/dpm/interaction/coupled-calculations? yes')
 ####################################################################################################################  

    fluentUnit.setNrIterations(10)
    fluentUnit.calculate()

 #################################################保存cgns后处理结果########################################################
    scheme.doMenuCommand("/file/export/cgns version_"+str(CFD_simu.count)+" no velocity dpm-concentration no")
    paraview_post_bat('F:/Thinking/program/pareto_front/Workdata/pic_result/', str(workPath)+'/version_'+str(CFD_simu.count)+'.cgns',
                        file_name1 = 'velocity_'+str(CFD_simu.count), file_name2 = 'dpm_'+str(CFD_simu.count))

 #####################################################保存结果########################################################
 
    run_id = str(CFD_simu.count)
    scheme.doMenuCommandToString('/report/fluxes/mass-flow no inlet* () yes simu_'+run_id+'.txt')#质量流量保存到文件里
    #scheme.doMenuCommandToString('/report/dpm-sample injection-0 () outlet () plane-16 () no no')
    scheme.doMenuCommandToString('/report/volume-integrals/volume-avg fuild () dpm-concentration yes dpm_'+run_id+'.txt')#质量浓度保存到文件里

    f = open(os.path.join(workPath,'simu_'+run_id+'.txt'), 'r', encoding='utf-8')
    line = f.read()
    item = line.split()
    mf_index = item.index('inlet')+1
    massflow = float(item[mf_index])

    d = open(os.path.join(workPath,'dpm_'+run_id+'.txt'), 'r', encoding='utf-8')
    dine = d.read()
    dpmem = dine.split()
    dpm_index = dpmem.index('fuild')+1
    contam = float(dpmem[dpm_index])

    

    return massflow, contam

def main():
    IND_size = 2
    # MIN = -10
    # MAX = 10
    #random.seed(64)

    creator.create('FitnessMin', base.Fitness, weights = (-1.0, -1.0))
    creator.create('Individual', list, fitness = creator.FitnessMin)   

    toolbox = base.Toolbox()

    def randomlist():
        return random.uniform(0,1)

    toolbox.register('attr_item', randomlist)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_item, n = IND_size)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)
    
    @CallingCounter
    def evaluate(individual):
        cfdv = individual[0]+individual[1]
        flow, contam = CFD_simu(velocity=cfdv, temperature = 293.15)
           
        return flow, contam

    toolbox.register("evaluate", evaluate)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)
    toolbox.register("select", tools.selNSGA2)

    # toolbox.decorate("mate", decorate.checkBounds(MIN, MAX))
    # toolbox.decorate("mutate", decorate.checkBounds(MIN, MAX))

    mstats = tools.Statistics(key=lambda ind: ind.fitness.values)
    mstats.register('avg', numpy.mean, axis = 0)
    mstats.register('std', numpy.std, axis = 0)
    mstats.register('min', numpy.min, axis = 0)
    mstats.register('max', numpy.max, axis = 0)

    CXPB = 0.7
    MUTPB = 0.2
    NGEN = 20
    MU = 10
    LAMBDA = 20

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, mstats,
                              halloffame=hof)

    return pop, mstats, hof

if __name__=='__main__':
 ##################################################################################
    now_time = time.strftime('%Y-%m-%d_%H-%M', time.localtime())
    cur_path =  os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path
    workPath =pathlib.Path(root_path+"/Workdata/Fluent_Python/"+now_time)

    folder1 = os.path.exists(workPath)

    if not folder1:
        os.makedirs(pathlib.Path(root_path+"/Workdata/Fluent_Python/"+now_time))

    aasFilePath = workPath/"aaS_FluentId.txt"
    for file in workPath.glob("aaS*.txt"):
        file.unlink()

    #fluent设置
    root_name = ["AWP_ROOT222","AWP_ROOT221","AWP_ROOT212","AWP_ROOT211","AWP_ROOT202","AWP_ROOT201","AWP_ROOT192","AWP_ROOT191",
                    "AWP_ROOT182","AWP_ROOT181","AWP_ROOT172","AWP_ROOT171","AWP_ROOT162","AWP_ROOT161","AWP_ROOT152","AWP_ROOT151"]
    fluent_exist = False
    for rn in root_name:
        env_exist = os.getenv(rn,'null')
        if env_exist != 'null':
            ansysPath = pathlib.Path(os.environ[str(rn)])
            fluent_exist = True
            break

    fluentExe = str(ansysPath/"fluent"/"ntbin"/"win64"/"fluent.exe")

    # 启动Fluent软件,使用-hidden可以隐藏fluent的GUI界面
    if fluent_exist:
        fluentProcess = subprocess.Popen(f'"{fluentExe}" 3ddp -aas -t4', shell=True, cwd=str(workPath))#-hidden
    else:
        error = 'no right fluent verison exist on this machine'
        starterror =  open(os.path.join(workPath,'startError.txt'),'w')
        starterror.write(error)
        starterror.close()
        sys.exit()

    # 监控aaS_FluentId.txt文件生成，等待corba连接
    while True:
        try:
            if not aasFilePath.exists():
                time.sleep(0.2)
                continue
            else:
                if "IOR:" in aasFilePath.open("r").read():
                    break
        except KeyboardInterrupt:
            sys.exit()
    # 初始化orb环境
    orb = CORBA.ORB_init()
    # 获得Fluent实例单元
    fluentUnit = orb.string_to_object(aasFilePath.open("r").read())
    scheme = fluentUnit.getSchemeControllerInstance()

    casename = 'F:/Thinking/CFD_study/case3/case3_files/dp0/FFF/MECH/FFF.1.msh'
    scheme.execScheme(f'(read-case "{casename}")')
    # udf_name1 = 'calculate_N_avg.c '
    # user_name2 = 'calculate_vd.c'
    # scheme.doMenuCommand('/define/user-defined/compiled-function/compile/libudf yes '
    #                        +str(udf_name1)+str(user_name2)+"    ") 
    # scheme.doMenuCommand('/define/user-defined/compiled-function load libudf')

    scheme.doMenuCommand("/define/model viscous ke-rng yes")
    scheme.doMenuCommand("/define/model energy yes no no no no")
    scheme.doMenuCommand("/define/operating-conditions gravity yes 0 9.8")
    scheme.doMenuCommand('/define/model/dpm/injections/create-injection injection-0 no yes surface no ub () '+ 
                        'no no no no no no no 0 0.6 0 1e-6 303.15 1e-3')
                        #                x速度 y速度 z速度 粒径 温度 流量
 ##################################################################################

    (p, sta, hof) = main()
    i = 0
    gen = []
    fit_flow = []
    fit_contam = []

    for ind in hof:
        i += 1
        fit_flow += [ind.fitness.values[0]]
        fit_contam += [ind.fitness.values[1]]
        gen += [i]

    fig, ax1 = plt.subplots()
    line1 = ax1.plot(fit_flow, fit_contam, "b-", label="CFD Paerto front")
    ax1.set_xlabel("flow")
    ax1.set_ylabel("contam", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    lns = line1
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    plt.show()