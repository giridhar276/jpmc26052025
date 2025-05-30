


import os
### delete xlsx files only
try:
    files = os.listdir()
    for file in files:
        if file.endswith("xlsx") and os.path.isfile(file):
            os.remove(file)
            print(file,"is deleted")
except Exception as err:
    print(err)