# fixed arguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments
def display(a = 0,b = 0,c = 0,d = 0):
    print(a,b,c,d)
display()
display(10)
display(10,20)
display(10,20,30)
display(10,20,30,40)

#variable length args
def display(*args):
    print(args)
    for val in args:
        print(val)
display(10,20,30,40,50,56,54,5,43,56,43,5,43,67,43,6,34,657,43,7434367,43,46,"python")



# task: read from file and insert all the records to databse

#lock1 : read the File 
#block2: validate
#block3:  db Connection 
#block4 : inserting records
#block5:  close connection