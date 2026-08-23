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

