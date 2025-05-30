#list
alist = [10,20,30]
alist[0] = 100
print("After changes",alist)

'''
# tuple
atup = (10,20,30)
atup[0] = 100
print("After making changes :" , atup)
'''

atup = (10,20,30)
# typecasting - converting from one object to another object
alist = list(atup)  
alist[0] = 1000
atup = tuple(alist) # reconverting back
print(atup)
