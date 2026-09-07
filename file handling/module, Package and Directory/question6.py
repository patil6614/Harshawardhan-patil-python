# Recursive Functions Main Program

from recursive_utils import factorial, fibonacci
from recursive_utils import sum_digits, binary

n = int(input("Enter a number: "))

print("Factorial:", factorial(n))
print("Sum of digits:", sum_digits(n))

if n == 0:
    print("Binary: 0")
else:
    print("Binary:", binary(n))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")