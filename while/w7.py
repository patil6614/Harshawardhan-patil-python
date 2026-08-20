#Print the smallest of n numbers
print(" smallest of n numbers")
n = int(input("Enter how many numbers: "))

i = 1
num = int(input("Enter number: "))
smallest = num

while i < n:
    num = int(input("Enter number: "))

    if num < smallest:
        smallest = num

    i = i + 1

print("Smallest number =", smallest)

