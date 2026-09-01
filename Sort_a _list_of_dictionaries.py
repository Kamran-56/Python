students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Aman", "marks": 92},
    {"name": "Riya", "marks": 78}
]

students.sort(key=lambda x: x["marks"], reverse=True)

for student in students:
    print(student)
