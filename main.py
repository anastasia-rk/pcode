from methods.prelimiraries import *
from methods.example_method import  *


if __name__ == '__main__':
   print("this it the main file, where all the imporant things are done")
   # check if we are using latex on this machine
   print(f"Using latex in figures: {plt.rcParams["text.usetex"]}")
   # show folders
   print("Folders:")
   print(dictionary_of_directories)