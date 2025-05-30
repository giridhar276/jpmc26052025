
#Write a program to tag each VM as 'Running' or 'Stopped' based on status.

infra = {
    "vm1": {"location": "Mumbai", "status": "Running"},
    "vm2": {"location": "Delhi", "status": "Stopped"},
    "vm3": {"location": "Hyderabad", "status": "Running"}
}


for key,value in infra.items():
    print(key)
    print("------")
    print("Status :",value['status'])
