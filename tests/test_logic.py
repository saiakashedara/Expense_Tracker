import os
from logic import add_expense, calculate_total, save_csv, load_csv, expenses


def setup_function():
    expenses.clear()


# ✅ Total calculation
def test_total_calculation():
    add_expense("Food", 100)
    add_expense("Travel", 50)
    assert calculate_total() == 150


# ✅ Invalid input handling
def test_invalid_amount():
    try:
        add_expense("Food", "abc")
        assert False
    except ValueError:
        assert True


# ✅ CSV save/load
def test_csv_save_load():
    add_expense("Food", 200)
    save_csv("test.csv")

    expenses.clear()
    load_csv("test.csv")

    assert calculate_total() == 200

    os.remove("test.csv")