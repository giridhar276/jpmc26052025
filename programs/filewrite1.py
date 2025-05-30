

# regular way # traditional way
fobj = open("customers.txt","w")

fobj.write("python programming\n")  # single string
fobj.write("unix shell\n")

fobj.writelines(["java\n","unix\n","oracle\n"])  # multiple strings

for val in range(1,100):
    fobj.write(str(val) + "\n")
fobj.close()