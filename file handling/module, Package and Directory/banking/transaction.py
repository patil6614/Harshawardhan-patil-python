# Transaction Module

def deposit(account, amount):
    account["balance"] = account["balance"] + amount


def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        return True
    else:
        return False