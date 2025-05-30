
alist = [45,67,23,64,83,81,38,61]
alist.append(100)          # single value
print("After appending :",alist)
alist.extend([91,29,53])   #multiple values
print("After extending:", alist)
alist.insert(0,10)         # list.insert(index,value)
print("After inserting :", alist)
alist.pop(1)               #list.pop(index)
print("After pop operation :",alist)
alist.pop()               #default is last index , value at last index is removed
print("After pop operation :",alist)
alist.remove(10000)          # 10 in the value in the list
print("After removing :",alist)
# validate it first and then remove
if 200 in alist:
    alist.remove(200)
    print("After removing :",alist)

alist.reverse()          # reversing in place
print("After reversing :",alist)
alist.sort()             # ascending
print("Afters sorting :",alist)
alist.sort(reverse=True)
print("After sorting in descending order:",alist)



# validation
alist = [45,67,23,64,83,81,38,61]
if 45 in alist:
    # some logical operation
    print(len(alist))


# iterating
for val in alist:
    print(val)

## reversing the list
for val in alist[::-1]:
    print(val)

# reversing the list
alist.reverse()
for val in alist:
    print(val)