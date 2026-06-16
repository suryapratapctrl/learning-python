import json
import os

# Load existing expenses 
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
else:
    expenses = []

# Add expenses
def add_expense():
    name = input("Enter description: ")
    amount = int(input("Enter amount: "))
    expenses.append({"description": name, "amount": amount})
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)
    print("Saved!")

# View expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
    else:
        for e in expenses:
            print(f"{e['description']} - {e['amount']}")

# Menu loop
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        break