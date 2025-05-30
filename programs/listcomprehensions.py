
alist = [10,20,30,40]     ##output:[15,25,35,45]
output = []
for val in alist:
    output.append(val + 5)
print(output)

#using list comprehension
#syntax
# object = [  expression  forloop]
alist = [10,20,30,40]
output = [  val + 5   for val in alist]  
print(output)

# display all even numbers
for val in range(1,10):
    if val % 2 == 0 :
        print(val)


# using list comprehension
evens = [   val   for val in range(1,10) if val %2 == 0]
print(evens)