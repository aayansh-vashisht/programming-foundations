# ELIF STATEMENTS


# Basic elif
age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")


# Multiple elif
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")


# Age categories
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age >= 5:
    print("Child")


# Grade calculator
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")


# Temperature check
temperature = float(input("Enter temperature: "))

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
elif temperature >= 5:
    print("Cold")


# Day check
day = input("Enter a day: ").strip().lower()

if day == "monday":
    print("Start of the week")
elif day == "friday":
    print("Almost weekend")
elif day == "saturday":
    print("Weekend")
elif day == "sunday":
    print("Weekend")


# Role check
role = input("Enter your role: ").strip().lower()

if role == "admin":
    print("Admin access")
elif role == "moderator":
    print("Moderator access")
elif role == "user":
    print("User access")


# Number check
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")


# Age range
age = int(input("Enter your age: "))

if age >= 60:
    print("Senior")
elif 18 <= age < 60:
    print("Adult")
elif 13 <= age < 18:
    print("Teenager")


# First matching condition runs
number = 10

if number > 0:
    print("Positive")
elif number == 10:
    print("Ten")


# Separate if statements
number = 10

if number > 0:
    print("Positive")

if number == 10:
    print("Ten")
