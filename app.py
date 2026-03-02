import tkinter as tk
from logic import add_expense, calculate_total, save_csv, load_csv

def add():
    try:
        category = category_entry.get()
        amount = amount_entry.get()

        add_expense(category, amount)

        listbox.insert(tk.END, f"{category} - ₹{amount}")
        total_var.set(f"Total: ₹{calculate_total():.2f}")

        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    except Exception as e:
        total_var.set(str(e))


def save():
    save_csv()
    total_var.set("Saved Successfully")


def load():
    listbox.delete(0, tk.END)
    data = load_csv()

    for cat, amt in data:
        listbox.insert(tk.END, f"{cat} - ₹{amt}")

    total_var.set(f"Total: ₹{calculate_total():.2f}")


root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add).pack()
tk.Button(root, text="Save CSV", command=save).pack()
tk.Button(root, text="Load CSV", command=load).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

total_var = tk.StringVar()
tk.Label(root, textvariable=total_var).pack()

root.mainloop()