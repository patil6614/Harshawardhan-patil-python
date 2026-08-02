
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(i)

  

n = int(input("Enter n: for even no. "))

print("Even numbers are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


n = int(input("Enter n: for odd no. "))

print("Odd numbers are:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)



n = int(input("Enter the value of n: for doubling series "))

num = 1

for i in range(n):
    if num > n:
        break
    print(num)
    num = num * 2

# Program to find the sum of
# 1 + 1/1! + 1/2! + ... + 1/n!

n = int(input("Enter the value of n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)


# Program to compute cos(x) using series

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(1, n + 1):
    fact = 1
    for j in range(1, 2 * i + 1):
        fact = fact * j

    term = (x ** (2 * i)) / fact
    sum = sum + sign * term
    sign = sign * -1

print("Cos(", x, ") =", sum)

#square root of number is prime or not

import math

n = int(input("Enter a number: for check square root is prime or not"))

root = int(math.sqrt(n))

flag = True

if root < 2:
    flag = False
else:
    for i in range(2, root):
        if root % i == 0:
            flag = False
            break

print("Square Root =", root)

if flag:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")


#design			A B C 
#			A B C 
#			A B C 

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

#for pattern
#      A
#      A B
#      A B C
#      A B C D 
#      A B C D E

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#for pattern
#A B C D E
#A B C D
#A B C
#A B
#A

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


#print the pattern
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5


n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#print the pattern
#      1
#      2 2
#      3 3 3
#      4 4 4 4 
#      5 5 5 5 5

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


    


    





        
