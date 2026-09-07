# Calculate student attendance percentage

f = open("attendance.txt", "r")

print("Students having attendance below 75%:")

for line in f:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    print(name, "-", percentage, "%")

    if percentage < 75:
        print("Below 75%")

f.close()