# Display file lines in reverse order

f = open("student.txt", "r")

lines = f.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line, end="")

f.close()