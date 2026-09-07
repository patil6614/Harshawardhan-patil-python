# String Utilities Main Program

from string_utils import count_vowels, reverse_string
from string_utils import palindrome, count_words, remove_spaces

s = input("Enter a string: ")

print("Number of vowels:", count_vowels(s))
print("Reverse:", reverse_string(s))

if palindrome(s):
    print("String is Palindrome")
else:
    print("String is not Palindrome")

print("Number of words:", count_words(s))
print("After removing spaces:", remove_spaces(s))