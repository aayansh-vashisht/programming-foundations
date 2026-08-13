from datetime import date

# Store expenses in a list
expenses = []

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

if __name__ == "__main__":
    # Test core functionality
    add_expense(expenses, 15.50, "Food", str(date.today()))
    add_expense(expenses, 45.00, "Transport", str(date.today()))
    list_expenses(expenses)
    print("Total Spent:", calculate_total(expenses))
