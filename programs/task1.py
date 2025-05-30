

filename = input("Enter any filename :")

if filename.endswith(".py"):
    print("python file")
elif filename.endswith(".java"):
    print("java file")
elif filename.endswith(".sh"):
    print("unix shell file")
else:
    print("unknown file")