# Count number of lines in a file

f = open("student.txt", "r")

count = 0

for line in f:
    count = count + 1

print("Total number of lines:", count)

f.close()