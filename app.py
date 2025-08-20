# Phase 2: Data persistence

# Save/load from JSON file,
# Basic error handling.

import json

def load_data():
    try:
        with open('expenses.txt', 'r') as file:
            demo = json.load()
            return demo
    except FileNotFoundError:
            return[]

def save_data(expenses):
    try:
        with open('expenses.txt', 'w') as file:
            json.dump(expenses, file, indent=2)
            print("Data saved successfully!")
    except Exception as e:
        print(f"Error while saving the data: {e}")        

# Phase 1: Core functionality

# Add expenses with amount, category, description, date,
# View all expenses,
# Simple text-based menu.

def add_expenses(expenses):
    amount = float(input("Enter amount: ")) # Convert to number.
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date: ")
    expenses.append({'amount': amount, 'category': category, 'description': description, 'date': date})
    save_data(expenses)

def list_all_expenses(expenses):
    if not expenses:
        print ("No expenses found")
        return

    print("\n")
    print("*" *70)
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

def main():
    expenses = load_data()
    while True:
        print("\n ^^^^^^^^^^^^^^ PERSONAL EXPENSE TRACKER ^^^^^^^^^^^^^^")
        print("Choose an option from below")
        print("1. List all Expenses")
        print("2. Add an Expense")
        print("3. Exit") 
        choice = input("Enter your choice: ")

        match choice: 
            case '1': 
                list_all_expenses(expenses)
            case '2':
                add_expenses(expenses)
            case '3':
                break
            case _:
                print("Invalid Choice")
                

if __name__ == "__main__":
    main()

# Phase 3: Analysis features

# Monthly spending summaries,
# Category-wise breakdown,
# Budget tracking.

# Phase 4: GUI (Optional)

# Charts/graphs with matplotlib.

# Phase 5: Advanced features

# Export to CSV/Excel,
# Recurring expenses,
# Multiple accounts.