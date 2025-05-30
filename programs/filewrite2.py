
# context manager
# if any line starts with keyword with ... we call that context maanger
# Advantage: if will be closed automatically.

# pythonic way
with  open("dataset.txt","w") as fobj:
    fobj.write("python programming\n")  # single string
    fobj.write("unix shell\n")

    fobj.writelines(["java\n","unix\n","oracle\n"])  # multiple strings

    for val in range(1,100):
        fobj.write(str(val) + "\n")


