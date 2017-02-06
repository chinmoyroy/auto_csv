import os
from os import listdir
from os import walk
from os.path import isfile, join
import csv
import MySQLdb
db1 = MySQLdb.connect(host="localhost",user="root",passwd="huh")
cursor = db1.cursor()
mypath=raw_input("Enter the path of the folder in which the csv's are located \n (without the traling /) \n")
db=mypath.split("/")[-1]
sql = 'CREATE DATABASE IF NOT EXISTS '+db
cursor.execute(sql)
sql= 'use '+db
cursor.execute(sql)
only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
table_names=[];
path_of_file=''
head=''
s=''
for i in only_files:
         i=i[:-4]
         path_of_file=mypath+'/'+i+'.csv'
         csv_data = csv.reader(file(path_of_file))
         table_name = i
         s=''
         for row in csv_data:
             createsqltable = 'CREATE TABLE IF NOT EXISTS ' + table_name +'('+' VARCHAR(100),'.join(row) + ' VARCHAR(100))'
            # print (createsqltable)
             cursor.execute(createsqltable)
             db1.commit()
             head=row
            # print(head)
             break
         query ='INSERT INTO '+table_name+' ('
         for i in range(0, len(head)):
              query = query + head[i]
              s=s+'"%s"'
              if i < len(head)-1:
                  s=s+', '

              if i < len(head) - 1:
                 query = query + ' ,'
         query=query+' ) VALUES('
         query=query+s+')'

         #sprint (query)
         for row in csv_data:

             cursor =db1.cursor()
#             print(query)
    #        row=','.join(row)
    #        query=query+row
             cursor.execute(query,row)
             db1.commit()
    #        print (query)
    ##        break

cursor.close()
