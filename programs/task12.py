

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


for key,value in employees.items():
    print("Name :",value['name'] )
    print("Department :",value['department'])
    print("-------------")


for value in employees.values():
    print(value['name'],value['department'])