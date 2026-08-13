# FORMATTED STRINGS


# Basic f-string
name = "Alex"

print(f"Hello {name}")


# Multiple variables
name = "Alex"
age = 20

print(f"My name is {name} and I am {age} years old")


# First and last name
first_name = "John"
last_name = "Smith"

print(f"Full name: {first_name} {last_name}")


# Calculations
a = 10
b = 5

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")


# Price calculation
price = 100
quantity = 3

print(f"Total: {price * quantity}")


# Decimal formatting
number = 3.14159265

print(f"1 decimal: {number:.1f}")
print(f"2 decimals: {number:.2f}")
print(f"3 decimals: {number:.3f}")


# Money formatting
price = 19.9999

print(f"Price: {price:.2f}")


# Percentage
score = 0.8567

print(f"Score: {score:.2%}")


# Large numbers
population = 123456789

print(f"Population: {population:,}")


# Large decimal number
money = 1234567.891

print(f"Amount: {money:,.2f}")


# String method inside f-string
name = "alex"

print(f"Uppercase: {name.upper()}")
print(f"Title case: {name.title()}")


# Boolean expression
age = 20

print(f"Adult: {age >= 18}")


# User input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, you are {user_age} years old")


# Future age
print(f"In 5 years you will be {user_age + 5}")


# Product calculator
product_price = float(input("Enter product price: "))
quantity = int(inpu# FORMATTED STRINGS


# Basic f-string
name = "Alex"

print(f"Hello {name}")


# Multiple variables
name = "Alex"
age = 20

print(f"My name is {name} and I am {age} years old")


# First and last name
first_name = "John"
last_name = "Smith"

print(f"Full name: {first_name} {last_name}")


# Calculations
a = 10
b = 5

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")


# Price calculation
price = 100
quantity = 3

print(f"Total: {price * quantity}")


# Decimal formatting
number = 3.14159265

print(f"1 decimal: {number:.1f}")
print(f"2 decimals: {number:.2f}")
print(f"3 decimals: {number:.3f}")


# Money formatting
price = 19.9999

print(f"Price: {price:.2f}")


# Percentage
score = 0.8567

print(f"Score: {score:.2%}")


# Large numbers
population = 123456789

print(f"Population: {population:,}")


# Large decimal number
money = 1234567.891

print(f"Amount: {money:,.2f}")


# String method inside f-string
name = "alex"

print(f"Uppercase: {name.upper()}")
print(f"Title case: {name.title()}")


# Boolean expression
age = 20

print(f"Adult: {age >= 18}")


# User input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, you are {user_age} years old")


# Future age
print(f"In 5 years you will be {user_age + 5}")


# Product calculator
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = product_price * quantity

print(f"Total price: {total:.2f}")


# Alignment
word = "Python"

print(f"{word:<10}")
print(f"{word:>10}")
print(f"{word:^10}")


# Show curly braces
print(f"{{Python}}")t("Enter quantity: "))

total = product_price * quantity

print(f"Total price: {total:.2f}")


# Alignment
word = "Python"

print(f"{word:<10}")
print(f"{word:>10}")
print(f"{word:^10}")


# Show curly braces
print(f"{{Python}}")
