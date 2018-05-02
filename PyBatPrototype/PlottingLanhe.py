import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as id
import AddSpecificCapacity
import FixUnevenLength            # Makes two list same length by removing or adding element
import sys                        # For exiting script among other
import ConvertToPandas
import Plotter
import accessingData
import PyBat
from PyBat import Database,Plots



CellKeys = ['NMC_std1_01_ECDEC','NMC_std1_02_ECDEC','NMC_std1_04_ECDEC','NMC_std1_05_ECDEC','NMC_std1_06_ECDEC','NMC_std1_07_ECDEC']


x = []
y = []
z = []

for index in range(0,len(CellKeys)):
    z.append(accessingData.accessingData(CellKeys[index], 'Cycle'))
    y.append(accessingData.accessingData(CellKeys[index], 'discharge_spec'))



NMC_std1_01 = accessingData.accessingDataframe(CellKeys[0])
NMC_std1_04 = accessingData.accessingDataframe(CellKeys[2])
NMC_std1_05 = accessingData.accessingDataframe(CellKeys[3])
NMC_std1_06 = accessingData.accessingDataframe(CellKeys[4])
NMC_std1_07 = accessingData.accessingDataframe(CellKeys[5])



#print(NMC_std1_04['discharge_spec'])

#print(NMC_std1_01)
NMC_average = NMC_std1_01['discharge_spec'] + NMC_std1_04['discharge_spec'] + NMC_std1_05['discharge_spec'] + NMC_std1_06['discharge_spec']+  NMC_std1_07['discharge_spec']
NMC_average = NMC_average.dropna(0)
NMC_average = NMC_average/5

NMC_average.to_pickle((Database + 'NMC_average_180426' + '.pkl'))




for index in range(0,len(NMC_average)):
    x.append(index)


plt.scatter(NMC_std1_01['Cycle'],NMC_std1_01['discharge_spec'], s=10)
plt.scatter(NMC_std1_04['Cycle'],NMC_std1_04['discharge_spec'], s=10)
plt.scatter(NMC_std1_05['Cycle'],NMC_std1_05['discharge_spec'], s=10)
plt.scatter(NMC_std1_06['Cycle'],NMC_std1_06['discharge_spec'], s=10)
plt.scatter(NMC_std1_07['Cycle'],NMC_std1_07['discharge_spec'], s=10)
plt.title('NMC(111) half cells')
plt.xlabel('Cycles')
plt.ylabel('Specific capacity [mAh/g]')
plt.savefig(Plots+'NMC/'+'NMC_average_180426.png')
plt.show()