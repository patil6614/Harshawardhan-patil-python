# Display complete contents of a file

f = open("student.txt", "r")

data = f.read()

print("File Contents:")
print(data)

f.close()