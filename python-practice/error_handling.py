# ERRORS AND DEBUGGING


# --------------------
# SYNTAX ERRORS
# --------------------

# Correct syntax
age = 20

if age >= 18:
    print("Adult")


# --------------------
# RUNTIME ERRORS
# --------------------

# This would cause ZeroDivisionError
# print(10 / 0)


# This would cause ValueError
# number = int("hello")


# --------------------
# LOGICAL ERRORS
# --------------------

length = 10
width = 5

# Wrong logic
wrong_area = length + width

print(wrong_area)


# Correct logic
area = length * width

print(area)


# --------------------
# BASIC TRY EXCEPT
# --------------------

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid integer")


# --------------------
# DIVISION ERROR
# --------------------

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print(result)

except ZeroDivisionError:
    print("You cannot divide by zero")


# --------------------
# MULTIPLE EXCEPT BLOCKS
# --------------------

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print(result)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# --------------------
# TRY EXCEPT ELSE
# --------------------

try:
    number = int(input("Enter another number: "))

except ValueError:
    print("Invalid number")

else:
    print(f"You entered {number}")


# --------------------
# TRY EXCEPT FINALLY
# --------------------

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number")

finally:
    print("This always runs")


# --------------------
# FULL STRUCTURE
# --------------------

try:
    number = int(input("Enter a whole number: "))

except ValueError:
    print("Invalid input")

else:
    print(f"Valid number: {number}")

finally:
    print("Finished")


# --------------------
# EXCEPTION INFORMATION
# --------------------

try:
    number = int("hello")

except ValueError as error:
    print(error)


# --------------------
# DEBUGGING WITH PRINT
# --------------------

price = 100
quantity = 3

total = price * quantity

print("price:", price)
print("quantity:", quantity)
print("total:", total)


# --------------------
# DEBUGGING A CONDITION
# --------------------

age = 20

print("Age:", age)
print("Condition:", age >= 18)

if age >= 18:
    print("Access allowed")


# --------------------
# RAISE AN EXCEPTION
# --------------------

def check_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


try:
    age = check_age(20)
    print(age)

except ValueError as error:
    print(error)


# --------------------
# DIVIDE FUNCTION
# --------------------

def divide(a, b):

    if b == 0:
        raise ValueError("Second number cannot be zero")

    return a / b


try:
    result = divide(10, 2)
    print(result)

except ValueError as error:
    print(error)


# --------------------
# VALID USER INPUT
# --------------------

while True:

    try:
        age = int(input("Enter your age: "))
        break

    except ValueError:
        print("Enter a valid whole number")

print(f"Your age is {age}")


# --------------------
# POSITIVE AGE CHECK
# --------------------

while True:

    try:
        age = int(input("Enter a positive age: "))

        if age < 0:
            raise ValueError("Age cannot be negative")

        break

    except ValueError as error:
        print(error)

print(f"Age accepted: {age}")
