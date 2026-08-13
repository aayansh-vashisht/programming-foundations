# MEMBERSHIP OPERATORS


# IN with string
text = "Python"

print("P" in text)
print("z" in text)


# NOT IN with string
text = "Python"

print("z" not in text)
print("P" not in text)


# Check word in sentence
message = "I am learning Python"

print("Python" in message)
print("Java" in message)


# Capital letters matter
message = "I Like Python"

print("Python" in message)
print("python" in message)


# Ignore capitalization
message = "I Like Python"

print("python" in message.lower())


# IN with if
email = "alex@gmail.com"

if "@gmail.com" in email:
    print("Gmail address")


# NOT IN with if
password = "hello123"

if "@" not in password:
    print("Password does not contain @")


# IN with list
fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
print("mango" in fruits)


# NOT IN with list
print("mango" not in fruits)


# Numbers in list
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)


# Weekend check
day = "Sunday"

if day in ("Saturday", "Sunday"):
    print("Weekend")
else:
    print("Weekday")


# User input
allowed_names = ["alex", "john", "sam"]

name = input("Enter your name: ").strip().lower()

if name in allowed_names:
    print("Access allowed")
else:
    print("Access denied")


# Check banned words
message = input("Enter a message: ").lower()

if "spam" in message:
    print("Spam word found")
else:
    print("No spam word found")


# Store result
fruits = ["apple", "banana"]

result = "apple" in fruits

print(result)
print(type(result))
