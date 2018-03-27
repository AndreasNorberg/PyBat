import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as id
#import ConvertToPandas
import GetColors
import GetLabels

########       Script for plotting data
## - Takes pickle name and variables to plot as input
## - Plots the specified x and y variables, with specified cycles (optional)
## - Will be improved!

def plotter(**kwargs):

    try:
        pickle_name = kwargs['pickle1']
    except:
        print ('Unrecognizable pickle!')
    try :
        cycles = kwargs['cycles1']
    except:
        try:
            cycles = kwargs['cycles2']
        except:
            cycles = None
    try:
        color_scheme = kwargs['color_scheme1']
    except:
        color_scheme = 'Blues'
    x1 = kwargs['x1']
    y1 = kwargs['y1']

    df = pd.read_pickle(pickle_name).astype(float)  # Reads pickle as float

    if (cycles==None):        # If no cycles are defined, will plot all cycles
            last_cycle = df.tail(1)['cycle'].as_matrix().astype(int)
            cycles = range(0, last_cycle[0], 1)   # Creates list from 0 to last cycle, increment 1

    color = GetColors.GetColors(df,cycles, color_scheme)     # Choose color maps from: https://matplotlib.org/examples/color/colormaps_reference.html

    for i in range(0, len(cycles)):
        df_cycle_x = df[df['cycle'] == cycles[i]]   # Make new data frame for given cycle
        plt.scatter(df_cycle_x[x1], df_cycle_x[y1], s=2, c=color[i])  # s = size

    try:        # Plotting second pickle if specified as input. Will be improved!
        pickle_name = kwargs['pickle2']
        try:
            cycles = kwargs['cycles2']
        except:
            cycles = None
        try:
            color_scheme = kwargs['color_scheme2']
        except:
            color_scheme = 'Blues'
        plotter(pickle1=pickle_name, cycles1= cycles, x1=x1, y1=y1, color_scheme=color_scheme)
    except:
        pass

    plt.xlabel(GetLabels.GetLabels(x1))
    plt.ylabel(GetLabels.GetLabels(y1))
    plt.show()

    return

#####    Script for testing function
##       Inputs:
#Location of data
pickle_name_1 = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\Pickles\B1_combi_t01_02_APC-THF_2_1Vto0_2V_0_01C'

# B1_combi_t02_01_APC-THF_2_4Vto0_2V_0_01C

##      Desired variable
x1 = 'cap_incr_spec'
y1 = 'potential'
cycles1 = [0, 1, 5, 10]
cycles2 = [20, 50, 100]
color_scheme1 = 'Greens'
color_scheme2 = 'Blues'
##      Outputs
#plotter(pickle1=pickle_name_1, x1=x1, y1=y1) # Without optional arguments, will plot all cycles in 'Blues' gradient.
plotter(pickle1=pickle_name_1, pickle2=pickle_name_1, cycles1= cycles1, cycles2=cycles2, x1=x1, y1=y1, color_scheme1=color_scheme1, color_scheme2=color_scheme2)

# Todo:
# - Clean up code
# - Remove second pop-up of graph window
# - User defined legend
# - User defined x-axis and y-axis values
# - Improve method of plotting multiple cells
# - Better color if plotting only one color
# - Multiple y-axis (e.g. Coloumbic efficiency or both charge and discharge)
