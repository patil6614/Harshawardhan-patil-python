# Student Result

import student

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
percent = student.percentage(marks)
grade = student.grade(percent)

print("\n--- STUDENT RESULT ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", grade)