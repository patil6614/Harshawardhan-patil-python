
#35-Accept a paragraph and count words according to their length
paragraph = input("Enter a paragraph: ")

words = paragraph.split()

length_count = {}

for word in words:

    length = len(word)

    length_count[length] = length_count.get(length, 0) + 1

print("Word length and number of words:", length_count)
