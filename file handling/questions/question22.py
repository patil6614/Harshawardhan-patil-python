
# Merge two text files

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter third file name: ")

f1 = open(file1, "r")
f2 = open(file2, "r")
f3 = open(file3, "w")

data1 = f1.read()
data2 = f2.read()

f3.write(data1)
f3.write("\n")
f3.write(data2)

f1.close()
f2.close()
f3.close()

print("Contents of both files copied successfully.")