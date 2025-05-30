#write a program to reverse a string without using [::-1]

text = input("Enter a string:")  #python
rev_text = ""
#print(text[::-1])

for char in text:
    rev_text = char + rev_text         
print("Reversed:",rev_text)

############### method2
for char in range(len(text),0,-1):    # range(6,0,-1)
    print(text[char-1],end="")      # text[6]
                             # text[4]

#p                p    
#y + p            yp
#t + yp           typ
#h  +  typ        htyp
#o  + htyp        ohtyp
#n + ohtyp        nohtyp
