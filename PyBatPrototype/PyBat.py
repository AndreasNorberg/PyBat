import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import ImportData as id
import AddSpecificCapacity
import FixUnevenLength            # Makes two list same length by removing or adding element
import sys                        # For exiting script among other
import ConvertToPandas
import Plotter
#import AccsessData
#Hidden functions in next line
## Functions
### Div

def ImportData(data_url, CellKey):
    return ConvertToPandas.biologic(data_url, CellKey)

def About(data_storage, CellKey):
    df = pd.read_pickle((data_storage + CellKey + '.pkl'))
    print(df.columns)
    return

#Locations of folders: Can be imported by writing "from PyBat import Database"
Database = 'C:/users/andnor/OneDrive - NTNU/Diatoma/Experimental/Database/'
CellDatabase = 'C:/users/andnor/OneDrive - NTNU/Diatoma/Experimental/Database/CellDatabase/'
Plots = 'C:/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Plots/'



#------------------------------General info-------------------------

print("Gi test)

#Innput:

Data = 'C:/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180430/Diatoma/180406/180406_SiO2MSC4_2_ECDEC_Hold48_2mV_CB4.mpt'
Cell ='SiO2MSC4_2'



#ConvertToPandas.biologic(Data, Cell, CellDatabase)
#ConvertToPandas.lanhe(Data,Cell, Database)
#About(Database,Cell)
#------------------------------Plotting------------------------------

#x1 = 'time'
#y1 = 'potential'


pickle_name_1 = CellDatabase +'SiO2MSC4_1.pkl'
pickle_name_2 = CellDatabase +'SiO2MSC4_2.pkl'


Plotter.plotter(pickle1=pickle_name_1, pickle2=pickle_name_2, x1='cap_incr_spec', y1='potential', legend=['Cell 1', 'Cell 2'], legend_loc=1)
#Plotter.plotter(pickle1=pickle_name_1, pickle2=pickle_name_2, x1='cap_incr_spec', y1='potential', cycles1=[0,1,5,10], color1='blue', color_scheme2='magma',legend=['Cell 1', 'Cell 2'], legend_loc=1)



#---------------------Accessing Data-------------------

#Data = 'potential'

#output = accessingData.accessingData(CellKey, Data)

#print(output)

