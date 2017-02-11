import os
import fileinput
from os import listdir
from os import walk
from os.path import isfile, join
import csv
import sys
mypath =raw_input("Enter the path of csv without the trailing / \n")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#onlyfiles contains the names of all csv files
fullpath=[]
path=mypath+'/'
for i in onlyfiles:
  fullpath.append(join(path,i))
#so now we have the full path of csv files
head=0
word_length=0
for i in fullpath:
   for line in fileinput.input(i, inplace=1):
          if fileinput.isfirstline():
                  line=line.replace(' ','_')
                  line=line.lower()
                  sys.stdout.write(line)
                  sys.stdout.flush()
          else:
                 sys.stdout.write(line)
                 sys.stdout.flush()

