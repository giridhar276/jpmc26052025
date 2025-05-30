name = "python_programming"
print(name.capitalize())
print(name.title())
print(name.replace("python","shell"))
#name = name.replace("python","shell") # this is permanent
print(name.split("_"))  #["python","programming"]
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.center(40))
print(name.center(40,"*"))
print(name.startswith("p"))
print(name.endswith("g"))
print(name.endswith("m"))
##############
# simple if 
############
if 1 < 2 :
    print("smaller")

if name.isupper():
    print("string is upper")
    print("inside if")
    print("still inside if")


if name.endswith("g"):
    print("String is lower")
    print("inside if")
##########
# if-else
###########
if name.isupper():
    print("string is upper")
    print("inside if")
else:
    print("string is lower")
    print("inside else")

################################
#if-elif-elif-elif-elif-elif-else
###################################
lang = input("Enter any language :")
lang = lang.lower()
if lang == "python":
    print("you are learning",lang)

elif lang == "java":
    print("you are learning",lang)
elif lang == "unix":
    print("you are learning", lang)

else:
    print("you are learning someother langauge")



aname = " python  "
print(len(aname))
print(aname.strip())
print(len(aname.strip()))  # remove whitespaces at both ends
print(len(aname.lstrip()))
print(len(aname.rstrip()))



### check for substring exists or not
name = "python programming"
print(name.find("ram"))  # if substring is found, it returns starting index
print(name.find("abc"))  # -1 if not found
if name.find("abc") !=  -1 :
    print("substring exists")
else:
    print("not found")


if "ram" in name:
    print("substring exists")
else:
    print("not found")



# range(start,stop,step)
for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(2,11,2):
    print(i)

for i in range(10,1,-1):
    print(i)

for i in range(10,1,-2):
    print(i)

name = "python"
for char in name:
    print(char)

name = "python"
for char in name:
    print(char,end=" ")

for i in range(10,1,-2):
    print(i,end="  ")



for i in range(10,1,-2):
    pass


name = "python"
for char in name[::-1]:
    print(char)