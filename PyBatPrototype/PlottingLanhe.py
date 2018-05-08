import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import StrToFloat
import ImportData as id
import AddSpecificCapacity
import FixUnevenLength            # Makes two list same length by removing or adding element
import sys                        # For exiting script among other
import ConvertToPandas
import Plotter
import AccessData
import PyBat
from PyBat import Database,Plots



CellKeys = ['NMC_std1_01_ECDEC','NMC_std1_02_ECDEC','NMC_std1_04_ECDEC','NMC_std1_05_ECDEC','NMC_std1_06_ECDEC','NMC_std1_07_ECDEC']


x = []
y = []
z = []

# for index in range(0,len(CellKeys)):
#     z.append(AccessData.AccessData(CellKeys[index], 'Cycle'))
#     y.append(AccessData.AccessData(CellKeys[index], 'discharge_spec'))


G1_average = AccessData.AccessCellData('G1_average')









plt.scatter(G1_average['Cycle'],G1_average['discharge_spec'], s=10)
plt.title('Average Capacity of graphite cells')
plt.xlabel('Cycles')
plt.ylabel('Specific capacity [mAh/g]')
plt.savefig(Plots+'NMC/'+'NMC_average_180426.png')
plt.show()