import os

#path =  os.getcwd()
path=raw_input("Enter the path without the trailing / \n")
#print(path)
filenames = os.listdir(path)

for filename in filenames:
	name = filename.replace(" ","_").lower()
	filename = os.path.join(path,filename)
	name = os.path.join(path,name)
	#print filename+"\n", name
	os.rename(filename, name)
