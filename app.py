# Phase 2: Data persistence

# Save/load from JSON file,
# Basic error handling.

import json
import matplotlib.pyplot as plt

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

# Phase 4: GUI (Optional)

# Charts/graphs with matplotlib.

def show_monthly_chart(expenses):
    if not expenses:
        print("No expenses to show")
        return
    
    monthly_totals = {}

    for expense in expenses:
        try:
            date_obj = datetime.strptime(expense['date'], "%d-%m-%Y")
            month_year = date_obj.strftime("%B-%Y")

            if month_year in monthly_totals:
                monthly_totals[month_year] += expense['amount']
            else:
                monthly_totals[month_year] = expense['amount']
        except ValueError:
            continue

    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

    plt.figure(figsize=(9,6))
    plt.bar(months, amounts)
    plt.title('Monthly Expenses')
    plt.xlabel('Months')
    plt.ylabel('Amounts')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    print("\n")
    print("*"*70)

def show_category_chart(expenses):
    if not expenses:
        print("No expenses to show")
        return
    
    category_totals = {}

    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else: 
            category_totals[category] = expense['amount']

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8,8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense by category")
    plt.show()

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

def update_expense(expenses):
    list_all_expenses(expenses)
    index = int(input("Enter the expense number to update: "))
    if 1 <= index <= len(expenses):
        amount = float(input("Enter amount to update: "))
        category = input("Enter category to update: ")
        description = input("Enter description to update: ")
        date = input("Enter date to update: ")
        expenses[index-1] = {'amount': amount, 'category': category, 'description': description, 'date': date}
        save_data(expenses)
    else:
        print("Invalid expense index selected")

def delete_expense(expenses):
    list_all_expenses(expenses)
    index = int(input("Enter the expense number to delete: "))
    if 1 <= index <= len(expenses):
        del expenses[index-1]
        save_data(expenses)
    else:
        print("Invalid expense index selected")

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
        print("3. Update an Expense")
        print("4. Delete an Expense")
        print("5. Monthly Summary")
        print("6. Category Wise Summary")
        print("7. Monthly Summary Chart")
        print("8. Category Summary Chart") 
        print("9. Exit")
        choice = input("Enter your choice: ")

        match choice: 
            case '1': 
                list_all_expenses(expenses)
            case '2':
                add_expenses(expenses)
            case '3':
                update_expense(expenses)
            case '4':
                delete_expense(expenses)
            case '5':
                monthly_expense(expenses)
            case '6':
                category_wise_monthly_summary(expenses)
            case '7': 
                show_monthly_chart(expenses)
            case '8':
                show_category_chart(expenses)
            case '9':
                break
            case '_':
                print("\n Invalid Choice")
                

if __name__ == "__main__":
    main()

# Phase 5: Advanced features

# Export to CSV/Excel,
# Recurring expenses,
# Multiple accounts.