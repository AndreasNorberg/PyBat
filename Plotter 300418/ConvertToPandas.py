# About scrip:
#-Takes a biologic txt file and convert the data into a pandas dataframe. The name of the colums is changed to global standard.

import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as id
import AddSpecificCapacity
import AddCycleCapacities


def biologic(data_url):

    Data, char_mass = id.importBiologic(data_url)                     # use ID:importBiologic to import data and the characteristic mass from a bilogic txt file.

    colum_names = Data[0][0:(len(Data[0])-1)]                         # Extracts the name of the colums from the txt file to place them in the dataframe

    df = pd.DataFrame(Data[1:],columns=colum_names)                   # Creates the dataframe

    del df['mode'],df['control changes'], df['Ns changes'],df['counter inc.'],df['Ns'],df['(Q-Qo)/mA.h'],df['control/V/mA'],df['Q charge/discharge/mA.h'],df['x'],df['control/V']       # Deletes row that we do not want.

    #colum_names = ['redox', 'error', 'time', 'dq','potential','halfcycle','energy_char','energy dis','capacitance_char','capacitance dis', 'current','discharge incr', 'charge incr','cap incr','current aim',	'cycle'	,'power']

    #Replaces the name of the colums with standard names-
    df = df.rename(columns={'ox/red':'redox', 'time/s':'time','dq/mA.h':'dq','Ecell/V':'potential','half cycle':'halfcycle','Energy charge/W.h':'energy_char','Energy discharge/W.h':'energy_dis','Capacitance charge/µF':'capacitance_char','Capacitance discharge/µF':'capacitance_dis','<I>/mA':'current', 'Q discharge/mA.h':'discharge_incr', 'Q charge/mA.h':'charge_incr','Capacity/mA.h' : 'cap_incr', 'Efficiency/%': 'QE', 'control/mA' : 'current_aim' ,'cycle number':'cycle','P/W': 'power'})

    df = AddSpecificCapacity.Incremental(df, char_mass)
    df = AddSpecificCapacity.Cyclebased(df, char_mass)

    return df

def lanhe(data_url):

    return


#Script for testing functions.

#data_url = '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'
#data_url = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\B1_combi_t01_02APC-THF_2_1Vto0_2V_0_01C_CE2.mpt'

#df = biologic(data_url)

#print(df['charge_spec'])

