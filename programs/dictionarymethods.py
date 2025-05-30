book = {"chap1":10 ,"chap2":20 ,"chap3":30,"chap1":100}
print(book)
## display individual value
print(book["chap10000"])
print(book["chap2"])

# add new key-value pair
book["chap4"] = 40
book["chap5"] = 50
print(book)

## keys
print(book.keys())

for k in book.keys():   # will display all th keys line by line
    print(k)

# values
print(book.values())

for v in book.values():
    print(v)

### items
print(book.items())

for k,v in book.items():
    print("Key :", k)
    print("value:", v)


## removing key-value from dictionary
book.pop("chap1")
print(book)

## last key value will be removed
book.popitem()
print(book)
book.popitem()
print(book)
book.popitem()
print(book)

## combining two dictionaries
book = {"chap1":10 ,"chap2":20 ,"chap3":30,"chap1":100}
newbook = {"chap8":80,"chap9":90}
finalbook = {**newbook,**book}
print(finalbook)

book.update(newbook)
print("updated dictionary :",book)  # book will be updated

# concatenating lists and strings
print([10,20] + [30,4])
print("hello" + "python")
print((10,20) + (30,40))


