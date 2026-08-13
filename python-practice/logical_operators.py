# LOGICAL OPERATORS


# AND operator
age = 20
has_id = True

print(age >= 18 and has_id)


# AND with false condition
age = 20
has_id = False

print(age >= 18 and has_id)


# OR operator
is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)


# NOT operator
is_raining = True

print(not is_raining)


# AND with if
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")
else:
    print("You cannot enter")


# OR with if
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend")
else:
    print("It is a weekday")


# NOT with if
logged_in = False

if not logged_in:
    print("Please log in")


# Check age range
age = 25

if age >= 18 and age <= 60:
    print("Age accepted")
else:
    print("Age not accepted")


# Chained comparison
age = 25

if 18 <= age <= 60:
    print("Age accepted")


# Discount check
age = 70

if age < 18 or age >= 65:
    print("You get a discount")
else:
    print("Regular price")


# Multiple conditions
age = 25
has_ticket = True
is_banned = False

if age >= 18 and has_ticket and not is_banned:
    print("You can enter")
else:
    print("You cannot enter")


# Parentheses
age = 16
has_parent = True

if age >= 18 or (age >= 13 and has_parent):
    print("You can watch the movie")
else:
    print("You cannot watch the movie")


# User input
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? yes/no: ").strip().lower()

if age >= 18 and has_ticket == "yes":
    print("You can enter")
else:
    print("You cannot enter")


# Login check
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


# Weekend check
day = input("Enter a day: ").strip().lower()

if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")


# NOT example
is_banned = False

if not is_banned:
    print("Access allowed")
else:
    print("Access denied")


# Logical operator priority
result = True or False and False

print(result)


# Same example with parentheses
result = True or (False and False)

print(result)
