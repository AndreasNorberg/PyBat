# About scrip:
#-Takes a biologic txt file and convert the data into a pandas dataframe. The name of the colums is changed to global standard.

import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
#import importData as id
#import Plotter
#import ConvertToPandas


def AddCycleCapacities(df, char_mass):

    # MOVED TO AddSpecificCapacity.Cyclebased

    return df

#Script for testing functions.

#data_url = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\B1_combi_t01_02APC-THF_2_1Vto0_2V_0_01C_CE2.mpt'
#pickle_name_1 = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\Pickles\B1_combi_t01_02_APC-THF_2_1Vto0_2V_0_01C'
#df = ConvertToPandas.biologic(data_url)
#df = AddCycleCapacities(df,3)
#Plotter.Plotter(pickle1=pickle_name_1, x1='cycle_nr', y1='discharge_spec')              # without optional argument 'cycles'


