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
