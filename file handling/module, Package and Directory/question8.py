# Student Report

from student.marks import total, percentage
from student.grade import grade
from student.attendance import attendance_percentage, eligible

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

present = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes: "))

total_marks = total(marks)
percent = percentage(marks)
student_grade = grade(percent)
attendance = attendance_percentage(present, total_classes)

print("\n--- STUDENT REPORT ---")
print("Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percent)
print("Grade:", student_grade)
print("Attendance:", attendance, "%")

if eligible(attendance):
    print("Attendance Status: Eligible")
else:
    print("Attendance Status: Not Eligible")