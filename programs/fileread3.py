'''write a proram to read empinfo.csv file and display all the UNIQUE workclasses.'''
import csv
workset = set()
with open("empinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    #processing
    for line in reader:
        workset.add(line[1])
    # displaying output
    for work in workset:
        print(work)

import csv
workdict = dict()
with open("empinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    #processing
    for line in reader:
        workdict[line[1]] = 1       # { "private":1 ,"public":1}
    # displaying output
    for work in workdict:
        print(work)