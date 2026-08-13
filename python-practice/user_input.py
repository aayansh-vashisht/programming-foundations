# USER INPUT


# Basic input
name = input("Enter your name: ")

print(name)


# Input with message
name = input("Enter your name: ")

print(f"Hello {name}")


# Integer input
age = int(input("Enter your age: "))

print(f"You are {age} years old")


# Age calculator
age = int(input("Enter your age: "))

future_age = age + 5

print(f"In 5 years you will be {future_age}")


# Float input
height = float(input("Enter your height: "))

print(f"Your height is {height}")


# Two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print(f"Total: {total}")


# Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")


# Full name
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(f"Your full name is {first_name} {last_name}")


# Price calculator
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total price: {total:.2f}")


# Yes or no input
answer = input("Are you a student? yes/no: ").lower()

is_student = answer == "yes"

print(is_student)


# Remove spaces
name = input("Enter your name: ").strip()

print(name)


# Combine strip and lower
answer = input("Do you like Python? yes/no: ").strip().lower()

print(answer == "yes")


# Even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Simple login
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


# Temperature check
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("It is hot")
else:
    print("It is not hot")


# Check input type
value = input("Enter something: ")

print(value)
print(type(value))
