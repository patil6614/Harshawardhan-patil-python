#33-Find the first character that occurs only once
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:

    if frequency[ch] == 1:
        print("First unique character:", ch)
        break

else:
    print("No unique character found")


