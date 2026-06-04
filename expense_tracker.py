import json
import os

FILE_NAME = "expenses.json"

# Load expenses
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']}")

# Total spending
def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spending: ₹{total}")

# Category-wise report
def category_report(expenses):
    report = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        report[category] = report.get(category, 0) + amount

    print("\n--- Category Report ---")
    for category, amount in report.items():
        print(f"{category}: ₹{amount}")

# Main Menu
def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spending(expenses)

        elif choice == "4":
            category_report(expenses)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()