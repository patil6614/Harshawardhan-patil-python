#Check whether the entered number is prime or not
print("number is prime or not")
n = int(input("Enter a number: "))

i = 2
count = 0

while i < n:
    if n % i == 0:
        count = count + 1
    i = i + 1

if n > 1 and count == 0:
    print("Number is Prime")
else:
    print("Number is Not Prime")


#Find the sum of digits of a given number
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)


#Check whether the entered number is palindrome or not
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")


#Reverse the given number
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)


#Print the multiplication table
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1


#Print the largest of n numbers
n = int(input("Enter how many numbers: "))

i = 1
num = int(input("Enter number: "))
largest = num

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    i = i + 1

print("Largest number =", largest)


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

