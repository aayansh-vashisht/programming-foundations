# Basic arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Print menu options for the user
def display_menu():
    print("\n--- Command-Line Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main execution loop
def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        # Exit program if option 5 is selected
        if choice == '5':
            print("Goodbye!")
            break

        # Get user numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Run corresponding function based on user selection
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
