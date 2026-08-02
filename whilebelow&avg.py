#Below average program
# print the natural numbers up to n
n = int(input("Enter the value of n: "))

i = 1
while i <= n:
    print(i)
    i += 1

#Print Even Numbers up to n
n = int(input("Enter n: "))

i = 2
while i <= n:
    print(i)
    i = i + 2

#Print Odd Numbers up to n
n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i)
    i = i + 2

#Sum of Natural Numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


#Average program
#Sum of odd numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1

print("Sum of odd numbers =", sum)

#Sum of even numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("Sum of even numbers =", sum)

#Natural numbers up to n in reverse order
n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n = n - 1

#Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i = i + 1

#Factorial of a given number
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)



    
    
    

    
