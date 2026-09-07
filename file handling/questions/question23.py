# Compare two text files

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

f1 = open(file1, "r")
f2 = open(file2, "r")

line_number = 0
different = False

while True:
    line1 = f1.readline()
    line2 = f2.readline()

    if line1 == "" and line2 == "":
        break

    line_number = line_number + 1

    if line1 != line2:
        print("Files are different.")
        print("First difference is at line:", line_number)

        print("File 1:", line1, end="")
        print("File 2:", line2, end="")

        different = True
        break

f1.close()
f2.close()

if different == False:
    print("Files are identical.")