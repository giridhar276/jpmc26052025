# method1
# reading the file line by line
# fobj acts like an handler or cursor for navigating
with open("languages.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

#method2
with open("languages.txt","r") as fobj:
    print(fobj.readlines())

with open("languages.txt","r") as fobj:
    for line in fobj.readlines():
        print(line)

# method3 : just like ctrl+a   ctrl+c  ctrcl+v
# genrally not suggested for bigger files
with open("languages.txt","r") as fobj:
    print(fobj.read())    # fobj.read() -----> string

#method4
import csv
with open("languages.txt","r") as fobj:
    reader = csv.reader(fobj) # converting file object to csv object
    for line in reader:
        print(line)  

