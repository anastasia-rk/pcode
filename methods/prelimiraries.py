import os
import sys
import shutil
import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pickle
import gc # garbage collector
from tqdm import tqdm

def check_for_executable(executable_name):
    # make sure executable is a string
    if not isinstance(executable_name, str):
        raise ValueError("executable must be a string")
    # check if executable exists on the machine
    executable_path = shutil.which("latex")
    if executable_path is None:
        print(f"no executable found for command: {executable_name}")
        return False
    else:
        print(f"path to executable found: {executable_path}")
        return True


# figure settings across the project
matplotlib.use('Agg')
plt.rcParams['figure.figsize'] = (20,10)
plt.rcParams['figure.dpi'] = 400
plt.rcParams['axes.facecolor']='white'
plt.rcParams['savefig.facecolor']='white'
plt.style.use("ggplot")
# check if we can use latex for figure text
latexInstalled = check_for_executable("latex")
if latexInstalled:
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]
            })
else:
    plt.rcParams.update({
        "text.usetex": False,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]
            })


# set up input and output directories in absolute paths
# get the current working directory
cwd = os.getcwd()
# remove the last folder from the path to make sure we are in the project folder
cwd = os.path.dirname(cwd)
# these prefixes will be used in all other files
dictionary_of_directories = {
    "input_data": os.path.join(cwd, "input_data"),
    "output_data": os.path.join(cwd, "output_data"),
    "figures": os.path.join(cwd, "figures"),
    "pickles": os.path.join(cwd, "pickles"),
    "tikzes": os.path.join(cwd, "tikzes")
}

# make sure all directories exist
for key, value in dictionary_of_directories.items():
    if not os.path.exists(value):
        os.makedirs(value)
        print(f"created directory: {value}")
    else:
        print(f"directory already exists: {value}")




if __name__ == '__main__':
   print("this it the preliminaries file.\n"
         " Here we are putting in some functions that will be used everywhere else in the project.\n"
         " We are also importing some libraries that will be used everywhere else in the project. \n")