import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set some environmental options
pd.set_option('display.max_columns', 100)
sns.set_theme(rc={'figure.figsize':(10,8)})

def create_plot(type, series, title, xlabel, ylabel, name_file, rotation=0, bottom=0.1, grid=True):
    """
    Function that plots a lineplot or boxplot, given a pandas Series.
    :param type: 'line' or 'box'
    :param series: series to plot
    :param title: plot title
    :param xlabel: x axis label
    :param ylabel: y axis label
    :param name_file: name of the file where to save the image (path to folder results/figures/ already set)
    :param rotation: rotation angle of x axis labels
    :param bottom: percentage of blank space under the plot in the image
    :param grid: boolean for tracing a grid under the plot
    """
    plt.clf()
    print(f"Plotting\n{series}")
    if type == 'line':
        sns.lineplot(series, marker='o')
    elif type == 'box':
        sns.boxplot(x=series)
    else:
        raise ValueError(f"type {type} not allowed. Choose between 'line' and 'box'")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.subplots_adjust(bottom=bottom)
    plt.grid(grid)
    plt.savefig('results/figures/'+name_file+'.png')
    #plt.show()