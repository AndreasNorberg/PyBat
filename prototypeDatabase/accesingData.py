import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as ID
import ConvertToPandas


#Innputs:
# Location of data
data_url = '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'

#Desired variable
variable = 'potential'






#Code

df = ConvertToPandas.biologic(data_url)

print(df[variable])
