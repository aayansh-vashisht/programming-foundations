# Command-Line Calculator

A clean, modular Python command-line calculator built with interactive menu loops, robust input validation, and zero-division handling.

---

## 🚀 Features

- **Basic Operations:** Addition, Subtraction, Multiplication, and Division.
- **Interactive CLI:** Menu-driven terminal loop allowing repeated calculations until exit.
- **Input Validation:** Gracefully handles invalid inputs (non-numeric values, invalid menu choices) without crashing.
- **Error Handling:** Safe division with built-in zero-division detection (`ZeroDivisionError` prevention).
- **Clean Architecture:** Modular, well-commented functions for easy maintenance and readability.

---

## 📂 Project Structure

```
01-calculator/
│
├── calculator.py   # Main calculator program
└── README.md       # Project documentation
```

---

## 🛠️ How to Run

1. **Prerequisites:** Make sure Python 3.x is installed on your system.
2. **Execute Script:** Run the script from your terminal:
   ```bash
   python calculator.py
   ```

---

## 💡 Usage Example

```text
==============================
    Command-Line Calculator   
==============================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Select an option (1-5): 1
Enter the first number: 10
Enter the second number: 5
--> Result: 10.0 + 5.0 = 15.0
```

---
