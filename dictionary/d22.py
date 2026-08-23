
#22-Create dictionary containing even numbers from 1 to 20 and their squares
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print("Even numbers and squares:", squares)

