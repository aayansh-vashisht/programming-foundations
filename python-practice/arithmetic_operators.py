# ARITHMETIC OPERATORS


# Addition
a = 10
b = 5

print(a + b)


# Subtraction
a = 20
b = 7

print(a - b)


# Multiplication
a = 6
b = 4

print(a * b)


# Division
a = 10
b = 2

print(a / b)


# Division with decimal result
print(9 / 2)


# Floor division
print(10 // 3)
print(17 // 5)


# Remainder
print(10 % 3)
print(17 % 5)


# Power
print(2 ** 3)
print(5 ** 2)


# Order of operations
answer = 10 + 5 * 2

print(answer)


# Parentheses first
answer = (10 + 5) * 2

print(answer)


# Arithmetic with variables
price = 50
quantity = 3

total = price * quantity

print(total)


# Even or odd check
number = 8

print(number % 2 == 0)


# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor division: {num1 // num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")


# Price calculator
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total: {total:.2f}")
