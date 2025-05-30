#write a program to print words longer than 4 characters in a sentence.

text = input("Enter a sentence:")

for word in text.split(" "):
    if len(word) > 4:
        print(word)
