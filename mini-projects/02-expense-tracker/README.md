# 💰 Expense Tracker

A simple, interactive command-line Expense Tracker built with Python. It allows users to track expenses by adding details such as amount, category, and date, list past expenses, calculate total spending, and persist data across sessions using JSON.

---

## 🚀 Features

- ➕ **Add Expense**: Record amount, category, and custom date (defaults to today's date if left blank).
- 📋 **List Expenses**: View all recorded expenses in a formatted, easy-to-read list.
- 💵 **Calculate Total**: Automatically compute total expenditures.
- 💾 **Data Persistence**: Automatically loads existing data on startup and saves changes to `expenses.json` on exit.
- 💻 **Interactive CLI Menu**: Simple terminal menu for quick interaction.

---

## 🛠️ Requirements

- Python 3.x
- No third-party dependencies required (uses built-in `json` and `datetime` modules).

---

## 📦 How to Run

1. Navigate to the project directory:
   ```bash
   cd mini-projects/02-expense-tracker
   ```

2. Run the application:
   ```bash
   python expense_tracker.py
   ```

---

## 🖥️ Usage Example

```text
=== EXPENSE TRACKER MENU ===
1. Add Expense
2. List Expenses
3. Show Total Spent
4. Save and Exit
Select an option (1-4): 1

Enter amount ($): 15.50
Enter category (e.g., Food, Transport): Food
Enter date (YYYY-MM-DD) [default: 2026-08-13]: 
Expense added successfully!
```

---

## 📁 File Structure

```text
02-expense-tracker/
│
├── expense_tracker.py   # Main Python script
├── expenses.json        # Auto-generated JSON file for storing expenses
└── README.md            # Project documentation
```
