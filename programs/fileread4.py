'''
write a proram to read empinfo.csv file and display the below output.

Total Male count   : xxxx
Total female count : xx
'''

import csv
mcount =0
fcount =0
with open("empinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    #processing
    for line in reader:
        line[9] = line[9].strip()
        if "Male" in line:
            mcount= mcount +1
        elif "Female" in line:
            fcount = fcount + 1
    print("Total male count :", mcount)
    print("Total female count :",fcount)