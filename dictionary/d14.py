
#14-Accept a string and find frequency of each character
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:", frequency)
