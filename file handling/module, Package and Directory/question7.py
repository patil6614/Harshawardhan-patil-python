# Main Program

from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import prime, palindrome, armstrong
from mathutils.statistics import mean, maximum, minimum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))

if b != 0:
    print("Division:", divide(a, b))

n = int(input("\nEnter a number: "))

print("Prime:", prime(n))
print("Palindrome:", palindrome(n))
print("Armstrong:", armstrong(n))

numbers = [10, 20, 30, 40, 50]

print("\nNumbers:", numbers)
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))