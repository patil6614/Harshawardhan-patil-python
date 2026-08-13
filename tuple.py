#1-Create a tuple of five integers and display it
t = (10, 20, 30, 40, 50)
print("Tuple:", t)

#2-Display first, last and third city
cities = ("Pune", "Mumbai", "Delhi", "Nashik", "Kolhapur")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

#3-cities = ("Pune", "Mumbai", "Delhi", "Nashik", "Kolhapur")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

#4-Check whether a color exists
colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter color: ")

if color in colors:
    print("Color exists")
else:
    print("Color does not exist")

#5-Display each fruit using a loop
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)

#6-Count repeated number
numbers = (10, 20, 10, 30, 10, 40, 20)

n = int(input("Enter number: "))

print("Count:", numbers.count(n))

#7-Find index of employee ID
ids = (101, 102, 103, 104, 105)

id = int(input("Enter employee ID: "))

if id in ids:
    print("Index:", ids.index(id))
else:
    print("ID not found")

#8-Concatenate two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t3 = t1 + t2

print("Combined tuple:", t3)

#9-Repeat tuple four times
t = (10, 20, 30)

print(t * 4)

#10-Tuple slicing operations
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five:", t[:5])
print("Last five:", t[5:])
print("Middle four:", t[3:7])
print("Alternate elements:", t[::2])
print("Reverse:", t[::-1])

#11-Convert tuple to list and add element
t = (10, 20, 30, 40)

l = list(t)
l.append(50)

t = tuple(l)

print(t)

#12-Accept five numbers and convert list into tuple
l = []

for i in range(5):
    n = int(input("Enter number: "))
    l.append(n)

t = tuple(l)

print("Tuple:", t)

#13-Modify tuple using list
t = (10, 20, 30, 40)

l = list(t)
l[1] = 200

t = tuple(l)

print("Modified tuple:", t)


#14-Delete a tuple completely
t = (10, 20, 30, 40)

del t

print("Tuple deleted successfully")


#15-Nested tuple of student details
students = (
    (101, "Rahul", 85),
    (102, "Amit", 90),
    (103, "Sneha", 88)
)

for student in students:
    print(student)

    
#16-Calculate sum of 10 numbers
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

total = sum(t)

print("Sum:", total)


#17-Largest and smallest without max() and min()
t = (25, 10, 45, 5, 30)

largest = t[0]
smallest = t[0]

for n in t:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)


#18-Calculate average
t = (10, 20, 30, 40, 50)

total = sum(t)
average = total / len(t)

print("Average:", average)


#19-Count even and odd numbers
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for n in t:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


#20-Check whether number exists
t = (10, 20, 30, 40, 50)

n = int(input("Enter number: "))

if n in t:
    print("Number exists")
else:
    print("Number does not exist")


#21-Store and display student details
student = (101, "Rahul", "CSE", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

    
#22-Employee information
employees = (
    (101, "Rahul", 30000),
    (102, "Amit", 35000),
    (103, "Sneha", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()

    
#23-Item prices
prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)

print("Total bill:", total)
print("Average price:", average)
print("Highest price:", max(prices))
print("Lowest price:", min(prices))

    
#24-Temperature of seven days
temp = (30, 32, 29, 35, 31, 33, 28)

print("Maximum temperature:", max(temp))
print("Minimum temperature:", min(temp))
print("Average temperature:", sum(temp) / len(temp))

    
#25-Runs scored in 10 matches
runs = (45, 60, 30, 75, 50, 90, 40, 65, 55, 80)

print("Total runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))


#26-Common elements between two tuples
t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = tuple(set(t1) & set(t2))

print("Common elements:", common)


#27-Merge two tuples and remove duplicates
t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

t3 = tuple(set(t1 + t2))

print("Merged tuple:", t3)


#28-Count frequency of each element
t = (10, 20, 10, 30, 20, 10, 40)

for n in set(t):
    print(n, "=", t.count(n))

    
#29-Sorted tuple ascending and descending
t = (50, 20, 40, 10, 30)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)


#30-Patient records and operations
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "A+"),
    (104, "Priya", 28, "O+")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
id = int(input("\nEnter Patient ID: "))

for patient in patients:
    if patient[0] == id:
        print("Patient Found:", patient)
        break
else:
    print("Patient not found")

# Count total patients
print("Total patients:", len(patients))

# Display patients by blood group
blood = input("Enter blood group: ")

print("Patients with", blood, "blood group:")

for patient in patients:
    if patient[3] == blood:
        print(patient)
