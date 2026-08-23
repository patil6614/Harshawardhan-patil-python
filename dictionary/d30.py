
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

