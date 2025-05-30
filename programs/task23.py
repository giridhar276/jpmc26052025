'''
write a script to create 10 directories in the current directory as below.

dir1
dir2
dir3
dir4
..
..
dir10
'''


import os
import sys
#os.mkdir("testdir11")
try:
    for value in range(1,11):
        dirname = "dir" + str(value)
        os.mkdir(dirname)
except Exception as err:
    print(err)
    print(sys.exc_info())