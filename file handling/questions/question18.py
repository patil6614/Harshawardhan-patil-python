# Employee records

def read_employees():
    f = open("employees.txt", "r")

    employees = []

    for line in f:
        data = line.strip().split(",")

        emp_id = data[0]
        name = data[1]
        department = data[2]
        salary = float(data[3])

        employees.append((emp_id, name, department, salary))

    f.close()

    return employees


def display_employees(employees):
    print("\nAll Employees:")

    for emp in employees:
        print(emp[0], emp[1], emp[2], emp[3])


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])

    print("\nHighest Paid Employee:")
    print(employee[1], "-", employee[3])


def average_salary(employees):
    total = 0

    for emp in employees:
        total = total + emp[3]

    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, amount):
    print("\nEmployees earning above", amount)

    for emp in employees:
        if emp[3] > amount:
            print(emp[1], "-", emp[3])


employees = read_employees()

display_employees(employees)
highest_paid(employees)
average_salary(employees)

amount = float(input("\nEnter salary limit: "))
above_salary(employees, amount)