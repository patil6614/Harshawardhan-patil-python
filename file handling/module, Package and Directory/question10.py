# Texttools Main Program

from texttools.cleaning import remove_punctuation
from texttools.cleaning import remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")

clean_text = remove_punctuation(text)
clean_text = remove_extra_spaces(clean_text)

print("\nCleaned Text:")
print(clean_text)

words = tokenize(clean_text)

print("\nTokens:")
print(words)

frequency = word_frequency(words)

print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)