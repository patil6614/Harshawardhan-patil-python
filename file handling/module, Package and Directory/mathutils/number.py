# Number Functions

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def palindrome(n):
    return str(n) == str(n)[::-1]


def armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total = total + int(digit) ** power

    return total == n