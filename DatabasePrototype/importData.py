# About scrip:
#-Imports a biologic data set from txt to a pandas dataframe.


import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat


# Function for importing data from Biologic
def importBiologic(data_url):                               #data_url is the location of data to be red.
    with open(data_url,'r') as file_input:
        Evaluater = False                                   # Evaluation variable used to determide where the data in the biologic tex file is. (We don't want to read all the junk in the begining of the document).
        char_mass = None
        Data = []                                           # Initiates a list to hold all data

        for line in file_input:                             # Reads the data from the data_url line by line.
            line = line.replace(",", ".")                   # Replaces "," with "." so that it is possible to convert the data from a string to a float.
            if Evaluater == True:                           # Evaluates if the line contains data or
                Data.append(line.split("\t"))               # Appendas data from a give line to the Data list
            elif line.find('Characteristic mass') == 0:     # Identifies the characteristic mass in the documet.
                char_mass = line.split(' ')[3]
            else:
                if line.find('mod') == 0 and line.find('ox/red'):
                    Data.append(line.split("\t"))
                    Evaluater = True

    file_input.close()
    return Data, char_mass


# Function for importing data from Lange
def importLanhe(data_url):

    return Data, char_mass



# # #Testing of functions
#
# data_url = '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'
# Data = importBiologic(data_url)
# print(Data[0][0])
















    ## Storing data in Pandas
    #col = Data[0][0:(len(Data[0])-1)]
    #
    # SiO2M_3 = pd.DataFrame(Data[1:],columns=col)
    # SiO2M_3.to_pickle('SiO2M_3_ECDEC.pkl')
    #
    # A  = SiO2M_3['Q charge/mA.h'].tolist()
    # print(A)
    #
    # x = strToFloat.strToFloat(SiO2M_3['time/s'].tolist())
    # y = strToFloat.strToFloat(SiO2M_3['Ecell/V'].tolist())
    #
    # print(type(x[1]))







    # Reading data from list of list (Will probably not be used)



    # #Initierer tom liste
    # x = []      # Time
    # y = []      # Potential
    #
    #
    # # Henter ut "time and potential" data fra txt fil.
    # for numb in range(2,len(Data)):
    #     x.append(float(Data[numb][7]))
    #     y.append(float(Data[numb][11]))








    #Plotter data som X og Y
    # plt.plot(x, y)
    # plt.xlabel('time [s]')
    # plt.ylabel('voltage [V]')
    # plt.title('About as simple as it gets, folks')
    # plt.grid(False)
    # plt.locator_params(axis='both', nbins=6)
    # plt.ylim(ymax=2.4)
    # plt.show()
    #





#Lukker filer for å spare minne.


