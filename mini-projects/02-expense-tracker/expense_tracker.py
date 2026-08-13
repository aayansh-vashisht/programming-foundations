import json
from datetime import date

# File to store expense data
FILE_NAME = "expenses.json"

# Function to add a new expense
def add_expense(expenses_list, amount, category, expense_date):
    expense = {
        "amount": amount,
        "category": category,
        "date": expense_date
    }
    expenses_list.append(expense)

# Function to list all recorded expenses
def list_expenses(expenses_list):
    if not expenses_list:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Expense List ---")
    for idx, item in enumerate(expenses_list, 1):
        print(f"{idx}. Date: {item['date']} | Category: {item['category']} | Amount: ${item['amount']:.2f}")

# Function to calculate total spent
def calculate_total(expenses_list):
    return sum(item["amount"] for item in expenses_list)

# Function to save data to JSON file
def save_expenses(expenses_list, filename=FILE_NAME):
    with open(filename, "w") as file:
        json.dump(expenses_list, file, indent=4)
    print("Expenses saved to file.")

# Function to load saved data at startup
def load_expenses(filename=FILE_NAME):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    # Load existing data on startup
    expenses = load_expenses()
    
    # Add an item and save
    add_expense(expenses, 15.50, "Food", str(date.today()))
    list_expenses(expenses)
    print("Total Spent:", calculate_total(expenses))
    save_expenses(expenses)
