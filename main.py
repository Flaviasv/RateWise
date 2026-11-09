import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calculator import calculate_total, calculate_per_person, apply_discount, calculate_after_costs
from database import save_quote


def calculate():
    hourly_rate = float(entry_rate.get())
    hours_per_class = float(entry_hours.get())
    classes_per_week = float(entry_classes.get())
    weeks = float(entry_weeks.get())
    rent = float(entry_rent.get())
    commute = float(entry_commute.get())
    num_people = int(entry_people.get())
    discount = float(entry_discount.get())

    total = calculate_total(hourly_rate, hours_per_class, classes_per_week, weeks, rent, commute)
    per_person = calculate_per_person(total, num_people)
    discounted = apply_discount(total, discount)
    after_costs = calculate_after_costs(total, rent, commute)

    result_total.set(f"${total:.2f}")
    result_per_person.set(f"${per_person:.2f}")
    result_discounted.set(f"${discounted:.2f}")
    result_after.set(f"${after_costs:.2f}")

def save():
    class_type_value = class_type.get()
    hourly_rate = float(entry_rate.get())
    hours_per_class = float(entry_hours.get())
    classes_per_week = float(entry_classes.get())
    weeks = float(entry_weeks.get())
    rent = float(entry_rent.get())
    commute = float(entry_commute.get())
    num_people = int(entry_people.get())
    discount = float(entry_discount.get())

    total = calculate_total(hourly_rate, hours_per_class, classes_per_week, weeks, rent, commute)
    per_person = calculate_per_person(total, num_people)
    discounted = apply_discount(total, discount)
    after_costs = calculate_after_costs(total, rent, commute)

    save_quote(class_type_value, num_people, weeks, classes_per_week, hours_per_class,
               rent, commute, hourly_rate, discount, total, per_person, after_costs)

    messagebox.showinfo("RateWise", "Quote saved!")

root = tk.Tk()
root.title("RateWise")
root.geometry("600x500")

# Class type (dropdown)
tk.Label(root, text="Class type").grid(row=0, column=0, sticky="w", padx=10, pady=5)
class_type = ttk.Combobox(root, values=["Private", "Group", "Corporate"], state="readonly")
class_type.set("Private")
class_type.grid(row=0, column=1, sticky="w", padx=10, pady=5)

# Number of people
tk.Label(root, text="Number of people").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_people = tk.Entry(root)
entry_people.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Classes per week
tk.Label(root, text="Classes per week").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_classes = tk.Entry(root)
entry_classes.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Weeks
tk.Label(root, text="Weeks").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_weeks = tk.Entry(root)
entry_weeks.grid(row=3, column=1, sticky="w", padx=10, pady=5)

# Hours per class
tk.Label(root, text="Hours per class").grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_hours = tk.Entry(root)
entry_hours.grid(row=4, column=1, sticky="w", padx=10, pady=5)

# Hourly rate
tk.Label(root, text="Hourly rate").grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=5, column=1, sticky="w", padx=10, pady=5)

# Rent / studio fee
tk.Label(root, text="Rent / studio fee").grid(row=6, column=0, sticky="w", padx=10, pady=5)
entry_rent = tk.Entry(root)
entry_rent.grid(row=6, column=1, sticky="w", padx=10, pady=5)

# Commute
tk.Label(root, text="Commute").grid(row=7, column=0, sticky="w", padx=10, pady=5)
entry_commute = tk.Entry(root)
entry_commute.grid(row=7, column=1, sticky="w", padx=10, pady=5)

# Discount (%)
tk.Label(root, text="Discount (%)").grid(row=8, column=0, sticky="w", padx=10, pady=5)
entry_discount = tk.Entry(root)
entry_discount.grid(row=8, column=1, sticky="w", padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save Quote", command=save).grid(row=14, column=0, columnspan=2, pady=10)

result_total = tk.StringVar()
result_per_person = tk.StringVar()
result_discounted = tk.StringVar()
result_after = tk.StringVar()

tk.Label(root, text="Total price:").grid(row=10, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, textvariable=result_total).grid(row=10, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Price per person:").grid(row=11, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, textvariable=result_per_person).grid(row=11, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Discounted price:").grid(row=12, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, textvariable=result_discounted).grid(row=12, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Amount after costs:").grid(row=13, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, textvariable=result_after).grid(row=13, column=1, sticky="w", padx=10, pady=5)

root.mainloop()