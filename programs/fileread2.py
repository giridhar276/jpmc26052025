

import csv
with open("empinfo.csv","r") as fobj:
    reader = csv.reader(fobj) # converting file object to csv object
    for line in reader:
        print(line[1])  
        print(line[3])
