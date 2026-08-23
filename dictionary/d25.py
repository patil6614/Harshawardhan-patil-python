
#25-Create dictionary containing student names and marks
students = {
    "Rahul": 80,
    "Amit": 90,
    "Sneha": 75
}

# Add a student
students["Priya"] = 85

# Update marks
students["Rahul"] = 88

# Delete a student
students.pop("Sneha")

# Search for a student
name = "Amit"

if name in students:
    print("Student found:", name, students[name])
else:
    print("Student not found")

# Display all students
print("All students:", students)

# Find highest marks
highest = max(students, key=students.get)
print("Highest marks:", highest, students[highest])

# Calculate average
average = sum(students.values()) / len(students)
print("Average marks:", average)

