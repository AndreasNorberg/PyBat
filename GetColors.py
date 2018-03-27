import numpy as np                # Matrise pakke
import pandas as pd               # Database pakke
import matplotlib.pyplot as plt   # Plottepakke
import strToFloat
import importData as id
import ConvertToPandas

########       Script for making list of color codes
## Takes optional color scheme as input
## Returns vector of colors to be used in plot

def GetColors(df, cycles=None, color_scheme=None):
    if color_scheme == None:     # Choose color maps from: https://matplotlib.org/examples/color/colormaps_reference.html
        color_scheme = 'Blues'

    if (cycles==None):        # If no cycles are defined, will plot all cycles
            last_cycle = df.tail(1)['cycle'].as_matrix().astype(int)
            cycles = range(0, last_cycle[0], 1)   # Creates list from 0 to last cycle, increment 1

    color_min = 100  # Minimum color (if zero, first color is almost white.
    color_max = 300  # Maximum color, 300 looks nice.
    color_nr = color_min  # Color for each plot (used in loop below)
    try:
        color_iter = int(
            (color_max - color_min) / (len(cycles) - 1))  # If e.g. 3 cycles, want 300-100 = 200, 200/2=100 iteration.
    except:
        color_iter = 0  # If only one cycle is plotted, will not need to change color. Need this exception to not divide by zero.

    color = []
    for i in range(0, len(cycles)):
        color.append(getattr(plt.cm, color_scheme)(color_nr))  # Setting color for given cycle
        color_nr = color_nr + color_iter  # Next color or color gradient

    return color

#####    Script for testing function
##       Inputs:
#Location of data (need dataframe to determine number of colors)
"""
pickle_name = '/Users\hennika\OneDrive - NTNU\PhD\Results\Cycling\Pickles\B1_combi_t01_02_APC-THF_2_1Vto0_2V_0_01C'
df = pd.read_pickle(pickle_name).astype(float)  # Reads pickle as float

##      Desired variables
cycles = [0, 1, 5, 10]

##      Outputs
colors = GetColors(df)        # For plotting all cycles
#colors = GetColors(df, cycles) # For plotting only specified cycles

x = range(0,1)
y = range(0,1)
for i in range(0, len(colors)):
    x = range(i,i+1)
    y = range(i,i+1)
    plt.scatter(x, y, s=1000, c=colors[i])  # s = size
plt.show()
"""