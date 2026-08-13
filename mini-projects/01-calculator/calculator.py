# Command-Line Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculator():
    result = None

    while True:
        print("\n--- Calculator ---")

        if result is None:
            try:
                result = float(input("Enter number: "))
            except ValueError:
                print("Invalid number")
                continue

        print(f"Current result: {result}")
        print("+  Add")
        print("-  Subtract")
        print("*  Multiply")
        print("/  Divide")
        print("c  Clear")
        print("q  Quit")

        operation = input("Choose operation: ").lower()

        if operation == "q":
            print("Calculator closed.")
            break

        if operation == "c":
            result = None
            continue

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue

        try:
            number = float(input("Enter number: "))
        except ValueError:
            print("Invalid number")
            continue

        # Perform calculation
        if operation == "+":
            result = add(result, number)
        elif operation == "-":
            result = subtract(result, number)
        elif operation == "*":
            result = multiply(result, number)
        elif operation == "/":
            result = divide(result, number)

        # Handle errors
        if isinstance(result, str):
            print(result)
            result = None
        else:
            print(f"= {result}")


calculator()
