import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke

# SECTIONS:
# ------------------------------------------------------
# Importing file
# Finding relevant data
# Plotting
# Differential capacity calculations (smoothing does not work)
# ------------------------------------------------------

########################################################
# Importing text file from your data folder  
########################################################

# Specify complete filename (including adress) here:
# Tips: as long as the first slash is slash (and not backslash), the rest of the slashes can be backslashes (I think).
Andreas = '/Users/andnor/OneDrive - NTNU/Diatoma/Experimental/Experimental data/Data Transfers/180226, DataTransfer/Diatoma, Biologic/180214/180214_SiO2MSC1_35CB_ECDEC_17_Hold120_2mV_CE5.mpt'
Henning = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\B1_combi_t01_02APC-THF_2_1Vto0_2V_0_01C_CE2.mpt'
datafile_path = Henning

# Reading file and saving everything to "Data"-variable. OBS: saving as strings, which need to be converted to numbers later!
with open(datafile_path,'r') as file_input:
    counter = 0                             # Counter to keep track of number of lines in file
    Data = []                               # initializing empty list for values (becomes list of list)

    new_path = 'data.txt'                   # Name of the text file where the values will be saved
    new_data = open(new_path, "w")          # initializing this new text file.
    mass_string = []                        # initializing variables
    mass = []
    for line in file_input:                     # Reading the input file, line for line
        if counter > 71:                        # Reading only from row 72, as the data starts here.
            this_line = line.replace(",", ".")  # Converting the commas to dots, so Python understand the scientific notation later
            new_data.write(this_line)           # Writing each line to new text file
            Data.append(this_line.split("\t"))  # Line shift in text file
        # Want to know the mass for specfic capacity:
        if "Characteristic mass" in line:       # Used for specific capacity. 
            mass_string = ((line.split('Characteristic mass : '))[1].split(' mg')[0]) # Extracting mass as string
            mass = (float(mass_string.replace(",", ".")))/1000  # Converting string to number and from mg to grams
        counter = counter + 1                   # Increase counter for each line read

    ##########################################################
    # Finding relevant data & converting it to numbers
    ##########################################################
    # Variable          Column nr
    # ----------------------------
    # Time (s)              07
    # Potential (V)         11
    # Capacity (mAh)        22

    # initializing variables
    uns_cap = []    # unspecific capacity (mAh). This is "stepwise" capacity (for each measurement)
    cap = []        # specific capacity (mAh/g). This is "stepwise" capacity (for each measurement)
    volt = []       # voltage   (V). Voltage for each measurement.
    num_rows = len(Data[:])             # len(Data[:]) will give all rows (values) of the variable
    # Converting to number (by float function) and appending the values from specified column to x and y.
    for numb in range(0,num_rows):
        uns_cap.append(float(Data[numb][22]))
        volt.append(float(Data[numb][11]))
    # Calculating specific capacity
    cap [:] = [x / mass for x in uns_cap]


    ##########################################################
    # Plotting voltage profile
    ##########################################################
    plt.xlabel('Capacity (mAh/g)')
    plt.ylabel('Voltage (V)')
    plt.title('Are we saving the world yet?')
    #plt.grid(True)
    plt.scatter(cap,volt, s=1)   # s = size, c=color, alpha=blending value [0-1]
    #plt.xlim(-1, 1)
    #plt.ylim(0, 2.1)
    plt.show()


    ##########################################################
    # Differential capacity plot
    ##########################################################
    # OBS: Remove """ in next line and """ at the bottom to run this part of the script
    """
    # Differential capacity = dQ/dE
    # Making arbitrary subgroup of data set for easier processing:
    volt_sub = volt[10000:20000]
    cap_sub  = cap [10000:20000]
    dQ = []         # Capacity difference between two measurements
    dE = []         # Voltage difference between two measurements
    volt_corr = []  # Need lists to be of same length for plotting. Use this voltage for diffcap variable
    diffCap = []    # Differential capacity between two measurements
    # Defining function for avoiding error if voltage difference is zero:
    def safe_div(x, y):
        if y == 0:
            return 0
        return x / y
    # Calculating differential capacity:
    for it in range (0, (len(volt_sub)-2)):         # Need to stop iterating before list is exceeded
        if (cap_sub[it+1] - cap_sub[it]) < 0:       # If this is true, we are changing charging to discharge/vice versa
            dQ.append(0)                            # Instead of weird extreme value, force to zero.
        dQ.append (cap_sub[it+1] - cap_sub[it])     # Capacity difference between two measurements
        dE.append (volt_sub[it+1] - volt_sub[it])   # Voltage difference between two measurements
        volt_corr.append(volt_sub[it])              # Need lists to be of same length for plotting. Use this voltage for diffcap variable
        diffCap.append (safe_div(dQ[it],dE[it]))    # Differential capacity between two measurements
    # Plotting with smoothing (smoothing does not work, commented out), from: https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot
    # from scipy.interpolate import spline    
    # xnew = np.linspace(min(volt_corr), max(volt_corr), 300)  # 300 represents number of points to make between x values
    # power_smooth = spline(volt_corr, diffCap, xnew)
    # plt.plot(xnew, power_smooth)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Differential capacity (mAh/g/V)')
    plt.title('Are we saving the world yet?')
    # plt.grid(True)
    plt.scatter(volt_corr, diffCap, s=1)  # s = size, c=color, alpha=blending value [0-1]
    plt.show()
    """
#--------------------------
# Closing files to save memory
new_data.close()
file_input.close()

