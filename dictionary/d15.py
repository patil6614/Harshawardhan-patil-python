#15-Accept a sentence and find frequency of each word
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)

