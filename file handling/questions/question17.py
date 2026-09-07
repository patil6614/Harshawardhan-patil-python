# Student records

f = open("students.txt", "r")

records = []

f.readline()   # Skip heading

for line in f:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    marks = int(data[2])

    records.append((roll, name, marks))

f.close()

print("All Student Records:")

for record in records:
    print(record[0], record[1], record[2])

# Highest marks
highest = max(records, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest[1], "-", highest[2])

# Average marks
total = 0

for record in records:
    total = total + record[2]

average = total / len(records)

print("Average marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")

for record in records:
    if record[2] > 80:
        print(record[1], "-", record[2])