# ELSE STATEMENTS


# Basic if else
age = 15

if age >= 18:
    print("Adult")
else:
    print("Under 18")


# Even or odd
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Positive or not positive
number = -5

if number > 0:
    print("Positive")
else:
    print("Not positive")


# Positive negative or zero
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Age categories
age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# Grade checker
score = 45

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Fail")


# Password check
password = input("Enter password: ")

if password == "python123":
    print("Correct password")
else:
    print("Wrong password")


# Login check
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


# Age input
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You can enter")
else:
    print("You cannot enter")


# Membership check
fruits = ["apple", "banana", "mango"]

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("Fruit found")
else:
    print("Fruit not found")


# Temperature check
temperature = float(input("Enter temperature: "))

if temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")


# Nested if else
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket")
else:
    print("You are too young")


# Number comparison
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is larger")
elif num1 < num2:
    print("Second number is larger")
else:
    print("Both numbers are equal")
