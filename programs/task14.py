
#Write a program to show student names with grades.

students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]

for student in students:  # each student is a list
    print(student['name'])
    print("-----------")
    for subject,marks in student['marks'].items():
        print(subject, marks)
    print()