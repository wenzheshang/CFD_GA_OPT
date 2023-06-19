from dymola.dymola_interface import DymolaInterface
from buildingspy.io.outputfile import Reader
from Counter_run_time import CallingCounter
import pandas as pd
import pathlib
import os

@CallingCounter
def simulate(**kwargs):
    
    dymola = DymolaInterface()
    k = kwargs

    try:
        ResultValue = []
        
        modelicaPath = pathlib.Path(os.environ["DymolaPath"])
        #Library import
        dirBuilding = os.path.join(modelicaPath,"Modelica/Library/Buildings-v8.0.0/Buildings 8.0.0")
        dirModelon = os.path.join(modelicaPath,"Modelica/Library/Modelon 2.6")
        #open Library
        dymola.openModel(path=os.path.join(dirBuilding, 'package.mo'))
        dymola.openModel(path=os.path.join(dirModelon, 'package.moe'))
        dymola.openModel(k['model'])
        problemName = k['problem_name']
        endT = k['endT']
            
        #第一次执行模拟时采用输入的初始变量进行初始化
        dymola_setName = k['variable']
        dymola_setValue = k['value']
        demo_name = 'demo_results'

        result = dymola.simulateExtendedModel(
            problem= problemName,
            startTime=0,
            stopTime=endT,
            numberOfIntervals=0,
            outputInterval=0.0,
            method="Dassl",
            tolerance=0.0001,
            fixedstepsize=0.0,
            resultFile=os.path.join(k['dir'], demo_name),
            initialNames=dymola_setName,
            initialValues=dymola_setValue,
            autoLoad=True
            )

        #self.multi_result_path_label.setText(demo_name)

    except:
        print('error1')
        log = dymola.getLastError()
        f =  open(os.path.join(k['dir'],'error1.txt'),'w')
        f.write(log)
        f.close()
        return

    try:
        status = result[0]

    except: 
        print('error2')
        log = dymola.getLastError()
        f =  open(os.path.join(k['dir'],'error2.txt'),'w')
        f.write(log)
        f.close()
        return
        
    if not status:
        print('error3')
        log = dymola.getLastError()
        f =  open(os.path.join(k['dir'],'error3.txt'),'w')
        f.write(log)
        f.close()
        return
    else:
        #成功模拟后输出结果部分,加保存excel功能
        #以下代码保存excel文件
        result_path = os.path.join(k['dir'],demo_name+'.mat')
        r = Reader(result_path,'dymola')

        result_name = 'reslut'+str(simulate.count)
    
        ResultVarName = r.varNames() #获取所有结果变量名
        for i in range(len(ResultVarName)):
            (t,r_ser) = r.values(ResultVarName[i])
            ResultValue.append(r_ser[-1])
        mydataframe = pd.DataFrame({'VarName':ResultVarName,'Value':ResultValue})
        mydataframe.to_csv(os.path.join(k['dir'], result_name+'.csv'))#将所有结果保存到.csv文件中，以备下次读取


        (te,energyconsumption) = r.values('EnergyConsumption')

    return energyconsumption[-1]
