# Create a file and write student information

f = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + semester + "\n")

f.close()

print("Student information written successfully.")