

#12-Find the student with the lowest marks
marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 88
}

lowest = min(marks, key=marks.get)

print("Lowest marks student:", lowest)
print("Marks:", marks[lowest])

