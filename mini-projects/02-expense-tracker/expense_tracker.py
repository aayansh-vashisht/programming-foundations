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
        print("\nNo expenses recorded yet.")
        return
    
    print("\n--- Expense List ---")
    for idx, item in enumerate(expenses_list, 1):
        print(f"{idx}. Date: {item['date']} | Category: {item['category']} | Amount: ₹{item['amount']:.2f}")

# Function to calculate total spent
def calculate_total(expenses_list):
    return sum(item["amount"] for item in expenses_list)

# Function to save data to JSON file
def save_expenses(expenses_list, filename=FILE_NAME):
    with open(filename, "w") as file:
        json.dump(expenses_list, file, indent=4)
    print("\nExpenses saved successfully!")

# Function to load saved data at startup
def load_expenses(filename=FILE_NAME):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main menu program loop
def main():
    # Load saved data at startup
    expenses = load_expenses()
    
    while True:
        print("\n=== EXPENSE TRACKER MENU ===")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Total Spent")
        print("4. Save and Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category (e.g., Food, Transport): ").strip()
                
                # Default to today's date if left blank
                expense_date = input(f"Enter date (YYYY-MM-DD) [default: {date.today()}]: ").strip()
                if not expense_date:
                    expense_date = str(date.today())
                    
                add_expense(expenses, amount, category, expense_date)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid number for amount.")
                
        elif choice == "2":
            list_expenses(expenses)
            
        elif choice == "3":
            total = calculate_total(expenses)
            print(f"\nTotal Spent: ₹{total:.2f}")
            
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose options 1 to 4.")

if __name__ == "__main__":
    main()
