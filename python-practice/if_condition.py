# IF STATEMENTS


# Basic if
age = 20

if age >= 18:
    print("You are an adult")


# Temperature check
temperature = 35

if temperature > 30:
    print("It is hot")


# Score check
score = 80

if score >= 50:
    print("You passed")


# Equal check
password = "python123"

if password == "python123":
    print("Correct password")


# Boolean check
is_raining = True

if is_raining:
    print("Take an umbrella")


# AND condition
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")


# OR condition
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# NOT condition
logged_in = False

if not logged_in:
    print("Please log in")


# Membership check
fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana found")


# String membership
message = "I love Python"

if "Python" in message:
    print("Python found")


# User input
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are an adult")


# Username check
username = input("Enter username: ").strip().lower()

if username == "admin":
    print("Welcome admin")


# Multiple if statements
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")

if number == 10:
    print("Number is 10")


# Check a range
score = int(input("Enter your score: "))

if 0 <= score <= 100:
    print("Valid score")


# Nested if
age = 20
has_ticket = True

if age >= 18:
    print("Age accepted")

    if has_ticket:
        print("Ticket accepted")


# Login check
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")


# Truthy string
name = "Alex"

if name:
    print("Name exists")


# Check user entered something
name = input("Enter your name: ").strip()

if name:
    print(f"Hello {name}")
