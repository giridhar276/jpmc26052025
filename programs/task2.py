#write a program to convert the string to uppercase only if its length is more than 10 characters else display the same string.

text = input("Enter a string :")

if len(text) > 10:
    print(text.upper())
else:
    print(text)