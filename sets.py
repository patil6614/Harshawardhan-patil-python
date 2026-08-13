# 1-Create a set containing five integers and display all its elements
s = {10, 20, 30, 40, 50}
print("Set:", s)


# 2-Create a list containing duplicate values and convert it into a set
numbers = [10, 20, 20, 30, 30, 40]
s = set(numbers)
print("Set after removing duplicates:", s)


# 3-Create a set of five fruits, add two new fruits
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Papaya")
print("Updated fruits:", fruits)


# 4-Create a set of numbers and remove a specified number
numbers = {10, 20, 30, 40, 50}
numbers.remove(30)
print("Set after removing 30:", numbers)


# 5-Create a set of student names and check whether student exists
students = {"Rahul", "Amit", "Sneha", "Priya", "Rohan"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set")
else:
    print("Student does not exist in the set")


# 6-Create a set of cities and find total number of cities
cities = {"Pune", "Mumbai", "Delhi", "Nashik", "Kolhapur"}
print("Total number of cities:", len(cities))


# 7-Create a set of programming languages and display each using for loop
languages = {"Python", "Java", "C++", "C", "JavaScript"}

print("Programming Languages:")
for language in languages:
    print(language)


# 8-Create a list containing duplicate numbers and remove duplicates using set
numbers = [10, 20, 20, 30, 40, 40, 50]
unique_numbers = set(numbers)
print("Numbers without duplicates:", unique_numbers)


# 9-Create two sets and find their union
set1 = {10, 20, 30}
set2 = {30, 40, 50}

print("Union:", set1.union(set2))


# 10-Create two sets and find common elements
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Common elements:", set1.intersection(set2))


# 11-Create two sets and find elements present only in each set
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Only in first set:", set1.difference(set2))
print("Only in second set:", set2.difference(set1))


# 12-Find elements present in either set but not in both
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Symmetric difference:", set1.symmetric_difference(set2))


# 13-Check whether first set is a subset of second set
set1 = {10, 20}
set2 = {10, 20, 30, 40}

print("Is first set subset of second set:", set1.issubset(set2))


# 14-Check whether first set is a superset of second set
set1 = {10, 20, 30, 40}
set2 = {10, 20}

print("Is first set superset of second set:", set1.issuperset(set2))


# 15-Check whether two sets have no elements in common
set1 = {10, 20, 30}
set2 = {40, 50, 60}

print("Are sets disjoint:", set1.isdisjoint(set2))


# 16-Check whether two sets are equal
set1 = {10, 20, 30}
set2 = {10, 20, 30}

print("Are both sets equal:", set1 == set2)


# 17-Two students have selected different subjects
student1 = {"Python", "Java", "Maths", "DBMS"}
student2 = {"Java", "Maths", "C++", "OS"}

print("Subjects studied by both students:",
      student1.intersection(student2))


# 18-Accept a sentence and display all unique words
sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)


# 19-Students present in morning and afternoon sessions
morning = {"Rahul", "Amit", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Rohan", "Neha"}

print("Students in both sessions:", morning.intersection(afternoon))
print("Only in morning:", morning.difference(afternoon))
print("Only in afternoon:", afternoon.difference(morning))
print("Present in at least one session:", morning.union(afternoon))


# 20-Students enrolled in Python and Java
python_students = {"Rahul", "Amit", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Rohan", "Neha"}

print("Python students:", python_students)
print("Java students:", java_students)


# 21-Find students enrolled in both courses and only one course
python_students = {"Rahul", "Amit", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Rohan", "Neha"}

print("Students in both courses:",
      python_students.intersection(java_students))

print("Students in only one course:",
      python_students.symmetric_difference(java_students))


# 22-Technical skills of two employees
employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "CSS"}

print("Common skills:", employee1.intersection(employee2))
print("Skills unique to Employee 1:", employee1.difference(employee2))
print("Skills unique to Employee 2:", employee2.difference(employee1))
print("All available skills:", employee1.union(employee2))


# 23-Available books and requested books
available_books = {"Python", "Java", "C++", "DBMS"}
requested_books = {"Python", "DBMS", "HTML"}

print("Requested books that are available:",
      available_books.intersection(requested_books))


# 24-Visitor IDs from two different days
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("Visitors only on first day:", day1.difference(day2))
print("Visitors only on second day:", day2.difference(day1))


# Products belonging to different categories
category1 = {"Laptop", "Mobile", "Tablet"}
category2 = {"Mobile", "Tablet", "Headphones"}

print("Products in both categories:",
      category1.intersection(category2))


# 25-Friends of two users
user1 = {"Rahul", "Amit", "Sneha", "Priya"}
user2 = {"Sneha", "Priya", "Rohan", "Neha"}

print("Mutual friends:", user1.intersection(user2))
print("Friends unique to User 1:", user1.difference(user2))
print("Friends unique to User 2:", user2.difference(user1))
print("Total unique friends:", len(user1.union(user2)))
