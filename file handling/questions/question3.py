# Append information to a file

f = open("student.txt", "a")

info = input("Enter additional information: ")

f.write("\n" + info)

f.close()

print("Information appended successfully.")