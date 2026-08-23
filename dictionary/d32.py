
#32-Find two numbers whose sum is equal to target
numbers = [2, 7, 11, 15]
target = 9

seen = {}

for number in numbers:

    required = target - number

    if required in seen:
        print("Two numbers:", required, number)
        break

    seen[number] = True
