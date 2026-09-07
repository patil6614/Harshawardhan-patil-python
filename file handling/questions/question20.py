# Calculate deposits, withdrawals and balance

f = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
balance = 0
largest = 0

for line in f:
    data = line.strip().split(",")

    transaction = data[0]
    amount = float(data[1])

    if amount > largest:
        largest = amount

    if transaction == "D":
        total_deposits = total_deposits + amount
        balance = balance + amount

    elif transaction == "W":
        total_withdrawals = total_withdrawals + amount
        balance = balance - amount

f.close()

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest)