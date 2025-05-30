

# fixed arguments
def display(a,b):  # single liner function
    c = a + b
    return c
total = display(10,20)
print(total)



# lambda function
# lambda is just the replacement of single liner function for faster execution
#syntax
#functioname = lambda variables : expression
display = lambda a,b : a + b
total = display(10,20)
print(total)


display = lambda *data : sum(data)
total = display(10,20,40,50,60,60)
print(total)

display = lambda a,b,c : a + b + c
total = display("python","programming","langauge")
print(total)