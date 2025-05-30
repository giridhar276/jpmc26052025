
### set operations 
aset = {10,10,20,30,30,30,30}
print(aset)
bset = {30,30,30,30,40,40,40,50}
print(bset)

print("Unique values:",aset.union(bset))
print("Common values :", aset.intersection(bset))
print("difference    :",aset.difference(bset))


aset.add(10)
print(aset)
aset.add(50)
print(aset)