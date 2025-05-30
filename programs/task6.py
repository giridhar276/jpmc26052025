#write a program to replace all the vowels in a string with *.


text = input("Enter  a string :")   #python
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char in vowels:
        result = result + "*"
    else:
        result = result + char   
print(result)


