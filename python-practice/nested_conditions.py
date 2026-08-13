# NESTED CONDITIONS


# Basic nested if
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")


# Nested if with inner else
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket")


# Outer else
age = 16
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket")
else:
    print("You are too young")


# Login check
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown username")


# User input
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? yes/no: ").strip().lower()

if age >= 18:
    if has_ticket == "yes":
        print("Access allowed")
    else:
        print("You need a ticket")
else:
    print("You must be 18 or older")


# Nested elif
membership = input("Enter membership: ").strip().lower()

if age >= 18:
    if membership == "gold":
        print("Gold access")
    elif membership == "silver":
        print("Silver access")
    else:
        print("Basic access")
else:
    print("Access denied")


# Positive and even che# NESTED CONDITIONS


# Basic nested if
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")


# Nested if with inner else
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket")


# Outer else
age = 16
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("You need a ticket")
else:
    print("You are too young")


# Login check
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown username")


# User input
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? yes/no: ").strip().lower()

if age >= 18:
    if has_ticket == "yes":
        print("Access allowed")
    else:
        print("You need a ticket")
else:
    print("You must be 18 or older")


# Nested elif
membership = input("Enter membership: ").strip().lower()

if age >= 18:
    if membership == "gold":
        print("Gold access")
    elif membership == "silver":
        print("Silver access")
    else:
        print("Basic access")
else:
    print("Access denied")


# Positive and even check
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Not positive")


# Three conditions
age = 20
has_ticket = True
is_banned = False

if age >= 18:
    if has_ticket:
        if not is_banned:
            print("Entry allowed")
        else:
            print("You are banned")
    else:
        print("Ticket required")
else:
    print("Too young")


# Simpler version
if age >= 18 and has_ticket and not is_banned:
    print("Entry allowed")


# Nested score check
score = int(input("Enter your score: "))

if score >= 50:
    print("You passed")

    if score >= 90:
        print("Excellent")
    elif score >= 75:
        print("Very good")
    else:
        print("Good")
else:
    print("You failed")ck
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Not positive")


# Three conditions
age = 20
has_ticket = True
is_banned = False

if age >= 18:
    if has_ticket:
        if not is_banned:
            print("Entry allowed")
        else:
            print("You are banned")
    else:
        print("Ticket required")
else:
    print("Too young")


# Simpler version
if age >= 18 and has_ticket and not is_banned:
    print("Entry allowed")


# Nested score check
score = int(input("Enter your score: "))

if score >= 50:
    print("You passed")

    if score >= 90:
        print("Excellent")
    elif score >= 75:
        print("Very good")
    else:
        print("Good")
else:
    print("You failed")
