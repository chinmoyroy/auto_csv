import os
from os import listdir
from os import walk
from os.path import isfile, join

mypath=raw_input("Enter the path of the folder in which the csv's are located \n (without the traling /) \n")
only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in only_files:
    path_of_file=mypath+'/'+i
    os.rename(path_of_file, path_of_file.replace(' ', '_'))
