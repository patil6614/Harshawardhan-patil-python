
#11-Find the student who has scored the highest marks
marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 88
}

highest = max(marks, key=marks.get)

print("Highest marks student:", highest)
print("Marks:", marks[highest])
