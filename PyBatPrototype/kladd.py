# About scrip:
#-Imports a biologic data set from txt to a pandas dataframe.


#import numpy as np                # Matrise pakke
#import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
#import strToFloat
#import convertToPandas
import accessingData


NMC_average = accessingData.accessingDataframe('NMC_average_180426')

x = []

for index in range(0,len(NMC_average)):
    x.append(index)



plt.scatter(x,NMC_average.values[:], s=10)
plt.show()





































