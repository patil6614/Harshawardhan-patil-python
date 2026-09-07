# Convert file contents to uppercase

f = open("student.txt", "r")
out = open("uppercase.txt", "w")

data = f.read()

out.write(data.upper())

f.close()
out.close()

print("Uppercase file created successfully.")