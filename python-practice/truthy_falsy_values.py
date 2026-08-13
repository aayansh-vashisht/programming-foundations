# TRUTHY AND FALSY VALUES


# Boolean values
print(bool(True))
print(bool(False))


# Numbers
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(0.0))
print(bool(3.5))


# Strings
print(bool(""))
print(bool("Python"))
print(bool("False"))
print(bool("0"))


# Lists
print(bool([]))
print(bool([1, 2, 3]))


# Tuples
print(bool(()))
print(bool((1, 2)))


# Dictionaries
print(bool({}))
print(bool({"name": "Alex"}))


# None
value = None

print(bool(value))


# Truthy string
name = "Alex"

if name:
    print("Name exists")


# Falsy string
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")


# Number check
number = 10

if number:
    print("Number is not zero")
else:
    print("Number is zero")


# Zero check
number = 0

if number:
    print("Number is not zero")
else:
    print("Number is zero")


# List check
items = ["apple", "banana"]

if items:
    print("List has items")
else:
    print("List is empty")


# Empty list
items = []

if not items:
    print("No items")


# User input
name = input("Enter your name: ").strip()

if name:
    print(f"Hello {name}")
else:
    print("You entered nothing")


# Username check
username = input("Enter username: ").strip()

if not username:
    print("Username cannot be empty")
else:
    print("Username accepted")


# Check None
result = None

if result is None:
    print("No result")


# Compare normal way
name = "Alex"

if name != "":
    print("Name exists")


# Cleaner truthy way
if name:
    print("Name exists")
