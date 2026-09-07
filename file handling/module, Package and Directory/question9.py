# Banking Main Program

from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan

name = input("Enter account holder name: ")
account_no = input("Enter account number: ")
balance = float(input("Enter opening balance: "))

account = create_account(name, account_no, balance)

print("\nCurrent Balance:", get_balance(account))

amount = float(input("Enter deposit amount: "))
deposit(account, amount)

print("Balance after deposit:", get_balance(account))

amount = float(input("Enter withdrawal amount: "))

if withdraw(account, amount):
    print("Withdrawal successful.")
else:
    print("Insufficient balance.")

print("Final Balance:", get_balance(account))

principal = float(input("\nEnter loan amount: "))
rate = float(input("Enter interest rate: "))
years = int(input("Enter loan period in years: "))

interest, total = calculate_loan(principal, rate, years)

print("Loan Interest:", interest)
print("Total Loan Amount:", total)