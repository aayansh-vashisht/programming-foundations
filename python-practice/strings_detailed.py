# STRINGS


# Create strings
name = "Alex"
message = "Hello Python"

print(name)
print(message)


# Indexing
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
print(word[-2])


# Slicing
print(word[0:3])
print(word[:3])
print(word[3:])
print(word[1:5])


# Slice with step
print(word[::2])


# Reverse string
print(word[::-1])


# String length
text = "Hello World"

print(len(text))


# Upper and lower
text = "Python"

print(text.upper())
print(text.lower())


# Title and capitalize
name = "john smith"

print(name.title())
print(name.capitalize())


# Remove spaces
name = "   Alex   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())


# Replace text
text = "I like Java"

print(text.replace("Java", "Python"))


# Find text
text = "Hello Python"

print(text.find("Python"))
print(text.find("Java"))


# Count characters
text = "banana"

print(text.count("a"))


# Starts and ends
filename = "photo.jpg"

print(filename.startswith("photo"))
print(filename.endswith(".jpg"))


# Split string
text = "apple banana mango"

words = text.split()

print(words)


# Split with comma
data = "Alex,20,Delhi"

parts = data.split(",")

print(parts)


# Unpack split values
name, age, city = data.split(",")

print(name)
print(age)
print(city)


# Join strings
words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)


# Join with comma
fruits = ["apple", "banana", "mango"]

print(", ".join(fruits))


# Join with dash
date_parts = ["09", "08", "2026"]

print("-".join(date_parts))


# Validate letters
print("Alex".isalpha())
print("Alex123".isalpha())


# Validate digits
print("12345".isdigit())
print("12.5".isdigit())


# Validate letters and numbers
print("Alex123".isalnum())
print("Alex_123".isalnum())


# Validate spaces
print("   ".isspace())
print("Hello".isspace())


# Check lowercase and uppercase
print("python".islower())
print("PYTHON".isupper())


# User age validation
age = input("Enter your age: ").strip()

if age.isdigit():
    print("Valid age")
else:
    print("Enter numbers only")


# Username validation
username = input("Enter username: ").strip()

if username.isalnum():
    print("Valid username")
else:
    print("Use letters and numbers only")


# Name validation
name = input("Enter your name: ").strip()

if name.isalpha():
    print("Valid name")
else:
    print("Use letters only")


# Membership
message = "I love Python"

if "Python" in message:
    print("Python found")


# Email check
email = input("Enter email: ").strip()

if "@" in email:
    print("Contains @")
else:
    print("Invalid email format")


# Basic f-string
name = "Alex"
age = 20

print(f"My name is {name} and I am {age} years old")


# Decimal formatting
price = 19.999

print(f"Price: {price:.2f}")


# Large number formatting
population = 1234567

print(f"Population: {population:,}")


# Percentage formatting
score = 0.85

print(f"Score: {score:.0%}")


# Strings cannot change by index
word = "Python"

word = "J" + word[1:]

print(word)
