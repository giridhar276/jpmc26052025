
#write a progarm to display all the files and directories
import os
try:
    files = os.listdir()
    for file in files:
        print(file)
except Exception as err :
    print(err)



#write a progarm to display all the files and directories from C:
import os
try:
    files = os.listdir("C:\\Users\\Public")
    for file in files:
        print(file)
except Exception as error :     # Default exception
    print(error)

#write a progarm to display all the files and directories from C:
import os
try:
    files = os.listdir("C:\\Users\\Public\\abc")
    for file in files:
        print(file)
except TypeError as err:
    print("Invalid operation")
except ValueError as err:
    print("Invalid input")
except (IndexError,KeyError) as err:
    print("Invalid index or key")
except FileNotFoundError as err:
    print("file or directory is not found",err)
except Exception as error :
    print(error)





