import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke



# Imprt av data fra url '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'

with open('/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt','r') as file_input:


    counter = 1                             # Counter for å holde orden på antall looper
    Data = []                               # Initierer tom liste for å holde på verdier (blir liste av liste)

    new_path = 'data.txt'                   # Lager navn .txt fil hvor lest data skal lagres.
    new_data = open(new_path, "w")          # Initierer ny txt fil
    title = "Data \n\n"                     # Tittel for ny txt fil
    new_data.write(title)                   # Skriver inn tittelen til txt fil

    for line in file_input:                 #leser innputfilen linje for linje for linje og lagrer den i ny txt fil.
        if counter > 70:                    #Stopper lesing etter 70 linjer (dette bare fordi jeg ikke gadd å ta med hele filen
            new_data.write(line)            #Skriver inn linje i txt fil
            Data.append(line.split("\t"))   #Linjeskift i txt fil


        counter = counter + 1

    # Write a for loop which runnes thorugh one column and create a list with only time and potential

    #Initierer tom liste
    x = []      # Time
    y = []      # Potential


    # Henter ut "time and potential" data fra txt fil.
    for numb in range(1,20):
        x.append(Data[numb][7])
        y.append(Data[numb][11])

    print(x)
    print(y)

    #Plotter data som X og Y
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.plot(x,y)
    plt.show()

    # for line in Data:
    #
    #     A = line
    #     new_data.write(A)

#Lukker filer for å spare minne.


new_data.close()
file_input.close()
