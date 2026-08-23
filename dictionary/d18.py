
#18-Find values that are common to both dictionaries
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "D": 20,
    "E": 30,
    "F": 40
}

common = set(dict1.values()) & set(dict2.values())

print("Common values:", common)

