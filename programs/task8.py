#write a progarm to count character frequencies:

text = input("Enter any text:")

for char in set(text):
    print(char ,":", text.count(char))