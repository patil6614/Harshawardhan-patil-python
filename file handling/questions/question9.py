# Count vowels and consonants

f = open("student.txt", "r")

data = f.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)

f.close()