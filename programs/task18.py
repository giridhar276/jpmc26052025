

#Write a program to list customers with balance over ₹10,000.


customers = {
    "C001": {"name": "Alice", "balance": 5000},
    "C002": {"name": "Bob", "balance": 12000},
    "C003": {"name": "Charlie", "balance": 3000}
}


for key,value in customers.items():
    if value['balance'] > 10000:
        print(value['name'])