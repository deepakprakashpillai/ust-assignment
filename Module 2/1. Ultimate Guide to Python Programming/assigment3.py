
students = [
    ("Alice", 20, (85, 90, 88)),
    ("Bob", 22, (78, 81, 74)),
    ("Charlie", 19, (92, 87, 85))
]

for student in students:
    avg_grade = sum(student[2]) / len(student[2])
    print(f"Name: {student[0]}, Average Grade: {avg_grade}")


top_student = max(students, key=lambda s: sum(s[2]) / len(s[2]))
print(
    f"Top Student: {top_student[0]}, Average Grade: {sum(top_student[2]) / len(top_student[2])}")
