from subprocess import run


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