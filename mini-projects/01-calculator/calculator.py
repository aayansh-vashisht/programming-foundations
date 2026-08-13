# Basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Division with error check for zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Function to safely get numbers from user without crashing
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Display available options
def display_menu():
    print("\n==============================")
    print("    Command-Line Calculator   ")
    print("==============================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

# Main program function
def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        # Exit program
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Validate menu choices
        if choice not in ('1', '2', '3', '4'):
            print("Invalid selection! Please choose an option from 1 to 5.")
            continue

        # Get inputs safely
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        # Perform calculation
        if choice == '1':
            print(f"--> Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"--> Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"--> Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"--> Result: {num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    main()
