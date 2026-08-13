# LOOPS


# Basic for loop
for number in range(5):
    print(number)


# Range from 1 to 5
for number in range(1, 6):
    print(number)


# Range with step
for number in range(0, 11, 2):
    print(number)


# Countdown with range
for number in range(5, 0, -1):
    print(number)


# Repeat text
for i in range(5):
    print("Hello")


# Loop through string
word = "Python"

for letter in word:
    print(letter)


# Loop through list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Multiply numbers
for number in range(1, 6):
    print(number * 2)


# Multiplication table
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Basic while loop
number = 1

while number <= 5:
    print(number)
    number += 1


# Countdown
number = 5

while number > 0:
    print(number)
    number -= 1

print("Go!")


# Password with while
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Correct password")


# Break
for number in range(1, 11):

    if number == 5:
        break

    print(number)


# Break with while
while True:
    answer = input("Type quit to stop: ").strip().lower()

    if answer == "quit":
        break

    print(f"You entered: {answer}")

print("Loop stopped")


# Continue
for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# Skip even numbers
for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)


# Find a number
numbers = [4, 8, 12, 16, 20]

for number in numbers:

    if number == 12:
        print("Found 12")
        break


# Nested loops
for i in range(3):

    for j in range(2):
        print(i, j)


# Rows and columns
for row in range(1, 4):

    for column in range(1, 4):
        print(row, column)


# Rectangle pattern
for row in range(4):

    for column in range(5):
        print("*", end="")

    print()


# Triangle pattern
for number in range(1, 6):
    print("*" * number)


# Nested multiplication tables
for number in range(1, 4):

    for multiplier in range(1, 6):
        print(f"{number} x {multiplier} = {number * multiplier}")

    print()


# User number loop
limit = int(input("Enter a number: "))

for number in range(1, limit + 1):
    print(number)


# Sum numbers
total = 0

for number in range(1, 6):
    total += number

print(f"Total: {total}")


# Even numbers
for number in range(1, 11):

    if number % 2 == 0:
        print(number)


# Stop at user number
stop_number = int(input("Enter stop number: "))

for number in range(1, 101):

    if number == stop_number:
        break

    print(number)
