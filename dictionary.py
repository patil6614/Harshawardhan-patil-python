#1-Create a dictionary containing student details and display all key-value pairs
student = {
    "Roll No": 101,
    "Name": "Rahul",
    "Department": "CSE",
    "Marks": 85
}

print("Student Details:", student)


#2-Create a dictionary containing employee information and display the value associated with a specified key
employee = {
    "ID": 101,
    "Name": "Amit",
    "Department": "IT",
    "Salary": 50000
}

print("Employee Name:", employee["Name"])


#3-Create a dictionary of five products and their prices. Add a new product and price
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}

products["Notebook"] = 80

print("Products:", products)


#4-Create a dictionary containing student marks and update the marks of a specified student
marks = {
    "Rahul": 75,
    "Amit": 80,
    "Sneha": 90
}

marks["Amit"] = 85

print("Updated Marks:", marks)


#5-Create a dictionary of cities and their populations. Remove a specified city
cities = {
    "Pune": 500000,
    "Mumbai": 2000000,
    "Delhi": 3000000,
    "Nashik": 400000
}

cities.pop("Nashik")

print("Cities:", cities)


#6-Ask the user for an employee ID and check whether it exists
employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


#7-Create a dictionary and find total number of key-value pairs
students = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90
}

print("Total key-value pairs:", len(students))


#8-Create a dictionary and display all keys, values and key-value pairs
data = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Pune"
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:", data.items())


#9-Create a dictionary of programming languages and their creators
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}

for language, creator in languages.items():
    print(language, ":", creator)


#10-Accept five student names and their marks and store them in a dictionary
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Students:", students)


#11-Find the student who has scored the highest marks
marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 88
}

highest = max(marks, key=marks.get)

print("Highest marks student:", highest)
print("Marks:", marks[highest])


#12-Find the student with the lowest marks
marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 88
}

lowest = min(marks, key=marks.get)

print("Lowest marks student:", lowest)
print("Marks:", marks[lowest])


#13-Calculate average marks of all students
marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 88
}

total = sum(marks.values())
average = total / len(marks)

print("Average marks:", average)


#14-Accept a string and find frequency of each character
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:", frequency)


#15-Accept a sentence and find frequency of each word
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


#16-Create two dictionaries and merge them
dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

dict1.update(dict2)

print("Merged dictionary:", dict1)


#17-Find keys that are common to both dictionaries
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 40,
    "C": 50,
    "D": 60
}

common = dict1.keys() & dict2.keys()

print("Common keys:", common)


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


#19-Create dictionary with duplicate values and remove duplicate values
data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

result = {}

for key, value in data.items():
    if value not in result.values():
        result[key] = value

print("Dictionary without duplicate values:", result)


#20-Display dictionary elements in ascending order of keys
data = {
    30: "C",
    10: "A",
    20: "B",
    40: "D"
}

result = dict(sorted(data.items()))

print("Ascending order:", result)


#21-Create dictionary containing numbers 1 to 10 and their squares
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print("Squares:", squares)


#22-Create dictionary containing even numbers from 1 to 20 and their squares
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print("Even numbers and squares:", squares)


#23-Create dictionary containing each unique number and its frequency
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Number frequency:", frequency)


#24-Create dictionary containing integers from 1 to 10 and their cubes
cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print("Cubes:", cubes)


#25-Create dictionary containing student names and marks
students = {
    "Rahul": 80,
    "Amit": 90,
    "Sneha": 75
}

# Add a student
students["Priya"] = 85

# Update marks
students["Rahul"] = 88

# Delete a student
students.pop("Sneha")

# Search for a student
name = "Amit"

if name in students:
    print("Student found:", name, students[name])
else:
    print("Student not found")

# Display all students
print("All students:", students)

# Find highest marks
highest = max(students, key=students.get)
print("Highest marks:", highest, students[highest])

# Calculate average
average = sum(students.values()) / len(students)
print("Average marks:", average)


#26-Create dictionary containing employee names and salaries
salaries = {
    "Rahul": 45000,
    "Amit": 60000,
    "Sneha": 55000,
    "Priya": 40000
}

highest = max(salaries, key=salaries.get)
lowest = min(salaries, key=salaries.get)
average = sum(salaries.values()) / len(salaries)

print("Highest salary:", highest, salaries[highest])
print("Lowest salary:", lowest, salaries[lowest])
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in salaries.items():
    if salary > 50000:
        print(name, salary)


#27-Create dictionary containing product names and quantities
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

# Add a product
products["Bottle"] = 8

# Update quantity
products["Book"] = 12

# Delete a product
products.pop("Pen")

# Search for a product
product = "Bag"

if product in products:
    print("Product found:", product, products[product])
else:
    print("Product not found")

# Display products with quantity below 10
print("Products with quantity below 10:")

for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)


#28-Create dictionary containing names and phone numbers
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

# Add contact
contacts["Sneha"] = "9876512345"

# Search contact
name = "Rahul"

if name in contacts:
    print("Contact found:", contacts[name])
else:
    print("Contact not found")

# Update contact
contacts["Amit"] = "9999999999"

# Delete contact
contacts.pop("Sneha")

# Display all contacts
print("All contacts:", contacts)


#29-Create dictionary containing book IDs and book names
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

# Add a book
books[104] = "DBMS"

# Search a book
book_id = 102

if book_id in books:
    print("Book found:", books[book_id])
else:
    print("Book not found")

# Remove a book
books.pop(103)

# Display all books
print("All books:", books)

# Count total books
print("Total books:", len(books))


#30-Group students according to their department
students = {
    "Rahul": "CSE",
    "Amit": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Rohan": "IT"
}

departments = {}

for name, department in students.items():

    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print("Students grouped by department:", departments)


#31-Group words according to their length
words = ["cat", "dog", "apple", "mango", "book", "pen"]

word_length = {}

for word in words:

    length = len(word)

    if length not in word_length:
        word_length[length] = []

    word_length[length].append(word)

print("Words grouped by length:", word_length)


#32-Find two numbers whose sum is equal to target
numbers = [2, 7, 11, 15]
target = 9

seen = {}

for number in numbers:

    required = target - number

    if required in seen:
        print("Two numbers:", required, number)
        break

    seen[number] = True


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


#34-Find the first character that occurs more than once
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:

    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break

else:
    print("No repeating character found")


#35-Accept a paragraph and count words according to their length
paragraph = input("Enter a paragraph: ")

words = paragraph.split()

length_count = {}

for word in words:

    length = len(word)

    length_count[length] = length_count.get(length, 0) + 1

print("Word length and number of words:", length_count)
