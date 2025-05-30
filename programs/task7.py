

text = input("Enter a string :")
upper = 0
lower = 0
digits= 0
for char in text:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isdigit():
        digits+=1
print("No. of upper chars:", upper)
print("No. of lower chars:", lower)
print("No. of digits:", digits)                      