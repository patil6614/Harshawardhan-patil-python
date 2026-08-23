#31-Group words according to their length
words = ["cat", "dog", "apple", "mango", "book", "pen"]

word_length = {}

for word in words:

    length = len(word)

    if length not in word_length:
        word_length[length] = []

    word_length[length].append(word)

print("Words grouped by length:", word_length)

