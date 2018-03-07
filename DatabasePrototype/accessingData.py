import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as id
import ConvertToPandas

########       Script for accessing data
## - Takes data_url (location of datafile) and variable (wanted data) as input
## - Returns a list with the data in float format.

def accessingData(data_url,variable):


    df = ConvertToPandas.biologic(data_url)

    output = strToFloat.strToFloat(df[variable].tolist())

    return output






#####    Script for testing function
##      Innputs:
#Location of data
data_url = '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'

##      Desired variable
variable1 = 'potential'
variable2 = 'time'

##      Outputs
output1 = accessingData(data_url,variable1)
output2 = accessingData(data_url,variable2)


print(variable1,':', output1[1],'\n', variable2,'    :', output2[1])



#Todo
#-Include pickeling of data
#-Include name of cell to dataframe.
