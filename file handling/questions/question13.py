# Search a word in a file

f = open("student.txt", "r")

search_word = input("Enter word to search: ")

count = 0
line_number = 0
line_numbers = []

for line in f:
    line_number = line_number + 1
    words = line.split()

    for word in words:
        if word.lower() == search_word.lower():
            count = count + 1
            line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

f.close()