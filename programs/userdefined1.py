

fobj = open("file1.txt","r")
fobj.close()

fobj = open("file2.txt","r")
fobj.close()


fobj = open("file3.txt","r")
fobj.close()


fobj = open("file4.txt","r")
fobj.close()


fobj = open("file5.txt","r")
fobj.close()


#######################################
import os
def readfiles(filename):
    fobj = open(filename,"r'")
    fobj.close()

files = os.listdir()
for filename in files:
    readfiles(filename)