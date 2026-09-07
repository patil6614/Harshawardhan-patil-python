# Student Module

def total_marks(marks):
    return sum(marks)


def percentage(marks):
    total = sum(marks)
    return total / len(marks)


def grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"