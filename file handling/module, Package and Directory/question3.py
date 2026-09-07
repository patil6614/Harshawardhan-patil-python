# Main Program

from number_utils import prime, palindrome, armstrong, perfect

n = int(input("Enter a number: "))

if prime(n):
    print("Number is Prime")
else:
    print("Number is not Prime")

if palindrome(n):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

if armstrong(n):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

if perfect(n):
    print("Number is Perfect")
else:
    print("Number is not Perfect")