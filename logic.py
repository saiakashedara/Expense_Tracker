import csv
import os

expenses = []

def add_expense(category, amount):
    if not category:
        raise ValueError("Category cannot be empty")

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be numeric")

    expenses.append((category, amount))
    return expenses


def calculate_total():
    return sum(amount for _, amount in expenses)


def save_csv(filename="expenses.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount"])
        writer.writerows(expenses)


def load_csv(filename="expenses.csv"):
    global expenses

    if not os.path.exists(filename):
        return []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        expenses = [(row["Category"], float(row["Amount"])) for row in reader]

    return expenses