import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from scipy.interpolate import griddata


#预整理数据部分

# ctm = []
# for i in range(1,375):
#     d = open(os.path.join('F:/Thinking/program/pareto_front/Workdata/Fluent_Python/2023-06-27_17-08','dpm_'+str(i)+'.txt'), 'r', encoding='utf-8')
#     dine = d.read()
#     dpmem = dine.split()
#     dpm_index = dpmem.index('fuildblock')+1
#     contam = float(dpmem[dpm_index])
#     ctm += [contam]

# df = pd.DataFrame({'contam': ctm})
# df.to_csv(os.path.join('F:/Thinking/program/pareto_front/Workdata/Fluent_Python/2023-06-27_17-08','_dpm.csv'))

# es = []
# for i in range(1,375):
#     e = pd.read_csv('F:/Thinking/program/pareto_front/Workdata/Dymola_python/2023-06-27_17-08/reslut'+str(i)+'.csv')
#     earray = np.array(e)
#     es += [earray[0][2]]
# df = pd.DataFrame({'Energy':es})
# df.to_csv(os.path.join('F:/Thinking/program/pareto_front/Workdata/Fluent_Python/2023-06-27_17-08','_es.csv'))
    

# 作图部分

data = pd.read_excel('F:/Thinking/Aircraft/opt/opt_test_3/VTTCEM.xlsx')
data2 = pd.read_excel('F:/Thinking/Aircraft/opt/opt_test_3/fit.xlsx')

#fit_flow = list(data2['fit_flow'])
fit_contam = list(data2['fit_contam'])
fit_energy = list(data2['fit_energy'])

fit_flow2 = list(data['Massflow'])
fit_contam2 = list(data['Contam'])
fit_energy2 = list(data['Energy'])

tem = list(data['inletT'])

colormap = []
map_vir = cm.get_cmap('Reds',128)

for i in range(len(tem)):
    color = (tem[i]-min(tem))/(max(tem)-min(tem))
    colormap += [color]

colormap = map_vir(colormap)
nor = plt.Normalize(min(tem)-0.5,max(tem)+1)    

fig, ax = plt.subplots(2, 1,figsize=(12,24))#, gridspec_kw={'height_ratios': [1,1,1]})

ax1 = ax[0]
line1 = ax1.scatter(fit_flow2, fit_contam2, color = colormap)#, "b-", label="CFD Paerto front 1")
#line2 = ax1.plot(fit_flow, fit_contam, "r-", label="CFD")

ax1.set_xlabel("flow(kg/s)")
ax1.set_ylabel("contam(kg/m3)", color="black")
for tl in ax1.get_yticklabels():
    tl.set_color("black")

# lns = line2
# labs = [l.get_label() for l in lns]
# ax1.legend(lns, labs, loc="center right")

sm = cm.ScalarMappable(norm=nor, cmap=map_vir)
plt.sca(ax[0])
cb = plt.colorbar(sm)
cb.ax.tick_params(labelsize = 12)
cb.set_label('Temperature(K)')
###############################################################################
ax2 = ax[1]
line3 = ax2.scatter(fit_flow2, fit_energy2, color = colormap)#, "b-", label="CFD Paerto front2")
#line4 = ax2.plot(fit_flow, fit_energy, "r-", label="CFD 2")
ax2.set_xlabel("flow(kg/s)")
ax2.set_ylabel("energy(W)", color="black")
for tl in ax2.get_yticklabels():
    tl.set_color("black")

# lns4 = line4
# labs4 = [l.get_label() for l in lns4]
# ax2.legend(lns4, labs4, loc="center right")

sm = cm.ScalarMappable(norm=nor, cmap=map_vir)
plt.sca(ax[1])
cb = plt.colorbar(sm)
cb.ax.tick_params(labelsize = 12)
cb.set_label('Temperature(K)')
################################################################################
# ax3 = ax
# line5 = ax3.scatter(fit_energy2, fit_contam2, color = colormap)#, "b-", label="CFD Paerto front3")
# line6 = ax3.plot(fit_energy, fit_contam, "r-", label="Pareto Front")
# ax3.set_xlabel("energy(W)")
# ax3.set_ylabel("contam(kg/m3)", color="black")
# for tl in ax3.get_yticklabels():
#     tl.set_color("black")

# lns6 = line6
# labs6 = [l.get_label() for l in lns6]
# ax3.legend(lns6, labs6, loc="center right")

# sm = cm.ScalarMappable(norm=nor, cmap=map_vir)
# plt.sca(ax3)#[2])
# cb = plt.colorbar(sm)
# cb.ax.tick_params(labelsize = 12)
# cb.set_label('Temperature(K)')
################################################################################
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.savefig('F:/Thinking/Aircraft/opt/opt_test_3/Figure_3.svg', dpi=900, format = 'svg')
plt.show()

#三维数据
# fitF = np.array(fit_flow)
# fitC = np.array(fit_contam)
# fitE = np.array(fit_energy)
# #fitF,fitC = np.meshgrid(fitF,fitC)
# #fitE = np.zeros(fitF.shape)
# N = 10
# [X,Y]=np.meshgrid(np.linspace(min(fitF),max(fitF),N),np.linspace(min(fitC),max(fitC),N))
# Z = griddata((fitF,fitC),fitE,(X,Y), method='cubic')

# # for i in range(fitF.shape[0]):
# #     for j in range(fitF.shape[1]):
# #         fitE[i,j] = fit_energy[i]

# fig = plt.figure(figsize=(12,5))
# ax = fig.add_subplot(1, 1, 1, projection='3d')
# ax.scatter(fit_flow2, fit_contam2, fit_energy2, color = colormap)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow)
# ax.set_xlabel('Flow(kg/s)')
# ax.set_ylabel('Contam(kg/m3)')
# ax.set_zlabel('Energy(W)')

# sm = cm.ScalarMappable(norm=nor, cmap=map_vir)
# plt.sca(ax)
# cb = plt.colorbar(sm)
# cb.ax.tick_params(labelsize = 12)
# cb.set_label('Temperature(K)')

# plt.savefig('F:/Thinking/Aircraft/opt/opt_test_new/Figure_3.svg', dpi=900, format = 'svg')

# plt.show()

#判断front序号
# number = []

# for i in range(len(fit_energy2)):
#     for j in range(len(fit_energy)):
#         if fit_energy2[i] == fit_energy[j]:
#             if fit_contam2[i] == fit_contam[j]:
#                 if fit_flow2[i] == fit_flow[j]:
#                     number += [i]
# dataframe = pd.DataFrame({'liteartion':number})
# dataframe.to_csv('F:/Thinking/Aircraft/opt/opt_test_new/literation.csv')
# print(number,len(number))

