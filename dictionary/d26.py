
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

