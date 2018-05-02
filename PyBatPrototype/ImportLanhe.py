# About scrip:
#-Loads lanhe data and returns a list Data and the characteristic mass. Data is a list of list with all data from the txt file.


import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat


# Function for importing data from Biologic
def importLanhe(data_url):                               #data_url is the location of data to be red.
    with open(data_url,'r') as file_input:
        Data = []                                          # Initiates a list to hold all data
        counter = 1

        for line in file_input:                             # Reads the data from the data_url line by line.
            line = line.replace(",", ".")                   # Replaces "," with "." so that it is possible to convert the data from a string to a float.
            line = line.rstrip()
            if counter > 1:                           # Evaluates if the line contains data or
                Data.append(line.split("\t"))               # Appendas data from a give line to the Data list
            counter = counter + 1

    file_input.close()
    return Data



# # #Testing of functions

#data_url = 'C:/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180424/180126_NMC_std1_08_ECDEC_005_3.txt'
#Data = importBiologic(data_url)



