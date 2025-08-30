# Phase 2: Data persistence

# Save/load from JSON file,
# Basic error handling.

import json

from datetime import datetime

def load_data():
    try:
        with open('expenses.txt', 'r') as file:
            demo = json.load(file)
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

# Phase 3: Analysis features

# Monthly spending summaries,
# Category-wise breakdown,
# Budget tracking.

def monthly_expense(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    
    monthly_totals = {}

    for expense in expenses:
        try:
            date_obj = datetime.strptime(expense['date'], "%d-%m-%Y")
            month_year = date_obj.strftime("%B %Y")

            if month_year in monthly_totals:
                monthly_totals[month_year] += expense['amount']
            else:
                monthly_totals[month_year] = expense['amount']

        except ValueError:
            print(f"Error while calcultaing monthly expense")

    print("\n")
    print("^^^^^^^^^^^^^^ MONTHLY SPENDING SUMMARY ^^^^^^^^^^^^^^")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")
    print("\n")
    print("*" *70)
    
def category_wise_monthly_summary(expenses):
    monthly_data = {}

    for expense in expenses:
        date_obj = datetime.strptime(expense['date'], "%d-%m-%Y")
        month_year = date_obj.strftime("%B %Y")

        if month_year not in monthly_data: 
            monthly_data[month_year] = {"total": 0, "categories": {}}

        monthly_data[month_year]["total"] += expense['amount']

        category = expense['category']

        if category in monthly_data[month_year]["categories"]:
            monthly_data[month_year]["categories"][category] += expense['amount']
        else:
            monthly_data[month_year]["categories"][category] = expense['amount']

    print("\n")
    print("^^^^^^^^^^^^^^ CATEGORY WISE MONTHLY SUMMARY ^^^^^^^^^^^^^^")
    for month, data in monthly_data.items():
        print(f"{month}: ${data['total']:.2f}")
        for category, amount in data['categories'].items():
            print(f"{category}: ${amount:.2f}")
        print("\n")
    print("*" *70)

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
    print("*" *70)

def main():
    expenses = load_data()
    while True:
        print("\n ^^^^^^^^^^^^^^ PERSONAL EXPENSE TRACKER ^^^^^^^^^^^^^^")
        print("Choose an option from below")
        print("1. List all Expenses")
        print("2. Add an Expense")
        print("3. Monthly Summaries")
        print("4. Category Wise Summary") 
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice: 
            case '1': 
                list_all_expenses(expenses)
            case '2':
                add_expenses(expenses)
            case '3':
                monthly_expense(expenses)
            case '4':
                category_wise_monthly_summary(expenses)
            case '5':
                break
            case _:
                print("\n Invalid Choice")
                

if __name__ == "__main__":
    main()

# Phase 4: GUI (Optional)

# Charts/graphs with matplotlib.

# Phase 5: Advanced features

# Export to CSV/Excel,
# Recurring expenses,
# Multiple accounts.