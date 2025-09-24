# Phase 2: Data persistence

# Save/load from JSON file,
# Basic error handling.

import json
import matplotlib.pyplot as plt
import csv

from datetime import datetime

def load_data():
    try:
        with open('expenses.txt', 'r') as file:
            demo = json.load(file)
            return demo
    except FileNotFoundError:
            return []

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

# Phase 5: Advanced features

# Export to CSV,
# Recurring expenses.

def export_to_csv(expenses):
    if not expenses:
        print("No expenses to export.")
        return
    
    try:
        with open ('expenses_export.csv', 'w', newline='', encoding='UTF-8') as file:
            fieldnames = ['Amount', 'Category', 'Description', 'Date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for expense in expenses:
                writer.writerow({
                    'Amount': expense['amount'],
                    'Category': expense['category'],
                    'Description': expense['description'],
                    'Date': expense['date']
                })
            print("Data exported to 'expenses_export.csv' successfully!")
    except Exception as e:
        print(f"Error exporting to excel {e}")

def load_recurring_data():
    try:
        with open('recurring_expenses.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_recurring_data(recurring_expenses):
    try:
        with open('recurring_expenses.txt', 'w') as file:
            json.dump(recurring_expenses, file, indent=2)
            print("Recurring data saved successfully")
    except Exception as e:
        print(f"Error while saving the recurring data: {e}")

def add_recurring_data(recurring_expenses):
    print("\n ADD RECURRING EXPENSES")

    name = input("Enter recurring data name: ")
    amount = float(input("Enter recurring data amount: "))
    category = input("Enter recurrnig data category: ")
    description = input("Enter recurring data description: ")

    print("\n FREQUENCY OPTIONS")   
    print("1. Monthly")
    print("2. Weekly")

    freq_choice = input("Enter frequency choice: ")

    if freq_choice == '1':
        frequency = 'Monthly'
        day = int(input("Enter day of month (1-31): "))
        recurring_expenses.append({
            'name': name,
            'amount': amount,
            'category': category,
            'description': description,
            'frequency': frequency,
            'day': day
        })
    
    elif freq_choice == '2':
        frequency = 'Weekly'
        day = input("Enter day of week (Monday, Tuesday, etc.)")
        recurring_expenses.append({
            'name': name,
            'amount': amount,
            'category': category,
            'description': description,
            'frequency': frequency,
            'day': day
        })

    else:
        print("Only monthly and weekly recurring expenses are supported for now")
        return
    
    save_recurring_data(recurring_expenses)
    print(f"Recurring Expense '{name}' Added!")

def delete_recurring_data(recurring_expenses):
    list_all_recurring_data(recurring_expenses)
    recurring_index = int(input("Enter the recurring expense to delete: "))
    if 1 <= recurring_index <= len(recurring_expenses):
        del recurring_expenses[recurring_index-1]
        save_recurring_data(recurring_expenses)
    else: 
        print("Invalid recurring index selected")

def list_all_recurring_data(recurring_expenses):
    if not recurring_expenses:
        print("No recurring expenses found")
        return
    
    print("\n")
    print("*" *70)
    for recurring_index, recurring_expenses in enumerate(recurring_expenses, start=1):
        print(f"{recurring_index}, Name: {recurring_expenses['name']}, Amount: {recurring_expenses['amount']}, Category: {recurring_expenses['category']}, Description: {recurring_expenses['description']}, Frequency: {recurring_expenses['frequency']}, Day: {recurring_expenses['day']}")
    print("*" *70)

def process_recurring_data(expenses, recurring_expenses):
    if not recurring_expenses:
        return expenses
    
    today = datetime.now()
    current_day = today.day
    current_weekday = today.strftime("%A")

    added_count = 0

    for recurring in recurring_expenses:
        should_add = False

        if recurring['frequency'] == 'Monthly' and recurring['day'] == current_day:
            already_added = False
            for expense in expenses:
                expense_date = datetime.strptime(expense['date'], "%d-%m-%Y")
                if (expense['description'] == f"{recurring['description']}" and expense_date.month == today.month and expense_date.year == today.year):
                    already_added = True
                    break

            if not already_added:
                should_add = True

        elif recurring['frequency'] == 'Weekly' and recurring['day'] == current_weekday:
            should_add = True

        if should_add:
            expenses.append({
                'amount': recurring['amount'],
                'category': recurring['category'],
                'description': recurring['description'],
                'date': today.strftime("%d-%m-%Y")
            })
            added_count += 1

    if added_count > 0:
        save_data(expenses)
        print(f"Added {added_count} recurring expense successfully")
    
    return expenses

def manage_recurring_data(recurring_expenses):
    while True:
        print("\n ^^^^^^^^^^^^^^^^ RECCURRING EXPENSES ^^^^^^^^^^^^^^^^")
        print("Choose an option from below")
        print("1. List all recurring data")
        print("2. Add a recurring data")
        print("3. Delete a recurring data")
        print("4. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_recurring_data(recurring_expenses)
            case '2':
                add_recurring_data(recurring_expenses)
            case '3':
                delete_recurring_data(recurring_expenses)
            case '4':
                break
            case _:
                print("\n Invalid choice")

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
    recurring_expenses = load_recurring_data()
    expenses = process_recurring_data(expenses, recurring_expenses)

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
        print("9. Export to CSV") 
        print("10. Manage Recurring Expenses")
        print("11. Exit")
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
                export_to_csv(expenses)
            case '10':
                manage_recurring_data(recurring_expenses)
            case '11':
                break
            case _:
                print("\n Invalid Choice")
                
if __name__ == "__main__":
    main()