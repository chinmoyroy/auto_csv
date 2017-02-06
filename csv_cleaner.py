'''the aim of this script is to load all csv's in a directory and remove spaces in its
headers so that they can be directly fed into another script for creation of mysql tables'''
import os
import fileinput
from os import listdir
from os import walk
from os.path import isfile, join
import csv
import sys
'''mypath =''
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#onlyfiles contains the names of all csv files
fullpath=[]
path=mypath+'/'
for i in onlyfiles:
    fullpath.append(join(path,i))
#so now we have the full path of csv files
head=0
word_length=0
for i in fullpath:'''
path=''

  for line in fileinput.input(path, inplace=1):
            if fileinput.isfirstline():
                    line=line.replace(' ','_')
                    line=line.lower()
                    sys.stdout.write(line)
                    sys.stdout.flush()
            else:
                   sys.stdout.write(line)
                   sys.stdout.flush()
#            csv_data = csv.reader(file(i))
#    for row in csv_data:
#           head=row
#           break
  #head has the original headers
    #print (head)
    for i in range(0, len(head)):
           row[i]=row[i].lower()
           row[i]=row[i].replace(" ","_")'''
''
