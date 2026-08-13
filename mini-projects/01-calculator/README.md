A simple Python command-line calculator that works like a basic handheld calculator. It keeps the current result and allows you to perform multiple calculations in a continuous loop.

🚀 Features
-Basic Operations: Addition, Subtraction, Multiplication, and Division.
-Continuous Calculation: Use the previous result for the next operation.
-Interactive CLI: Calculator stays active until you choose to quit.
-Clear Function: Reset the current result and start a new calculation.
-Input Validation: Handles invalid numbers and operations without crashing.
-Zero-Division Handling: Prevents division by zero.
-Clean Functions: Each mathematical operation is handled by its own function.

📂 Project Structure
01-calculator/
│
├── calculator.py   # Main calculator program
└── README.md       # Project documentation

🛠️ How to Run
Prerequisites
Make sure Python 3.x is installed.
Run the Program
Open your terminal inside the project folder and run:
python calculator.py

💡 Usage Example
--- Calculator ---

Enter number: 10

Current result: 10.0
+  Add
-  Subtract
*  Multiply
/  Divide
c  Clear
q  Quit

Choose operation: +
Enter number: 5
= 15.0

Current result: 15.0
+  Add
-  Subtract
*  Multiply
/  Divide
c  Clear
q  Quit

Choose operation: *
Enter number: 2
= 30.0

Current result: 30.0
+  Add
-  Subtract
*  Multiply
/  Divide
c  Clear
q  Quit

Choose operation: q
Calculator closed.
