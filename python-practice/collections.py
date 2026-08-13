# COLLECTIONS


# --------------------
# LISTS
# --------------------

# Create a list
fruits = ["apple", "banana", "mango"]

print(fruits)


# Access values
print(fruits[0])
print(fruits[1])
print(fruits[-1])


# Change a value
fruits[1] = "orange"

print(fruits)


# Add to end
fruits.append("grape")

print(fruits)


# Add at position
fruits.insert(1, "banana")

print(fruits)


# Remove by value
fruits.remove("orange")

print(fruits)


# Remove last item
removed = fruits.pop()

print(removed)
print(fruits)


# List length
print(len(fruits))


# Membership
print("apple" in fruits)


# Loop through list
for fruit in fruits:
    print(fruit)


# List methods
numbers = [5, 2, 8, 2]

print(numbers.count(2))
print(numbers.index(8))

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers)


# --------------------
# TUPLES
# --------------------

# Create a tuple
colors = ("red", "green", "blue")

print(colors)


# Access values
print(colors[0])
print(colors[-1])


# Loop through tuple
for color in colors:
    print(color)


# Tuple methods
numbers = (10, 20, 20, 30)

print(numbers.count(20))
print(numbers.index(30))


# One item tuple
single = (10,)

print(type(single))


# Tuple unpacking
person = ("Alex", 20)

name, age = person

print(name)
print(age)


# --------------------
# DICTIONARIES
# --------------------

# Create a dictionary
person = {
    "name": "Alex",
    "age": 20,
    "city": "Delhi"
}

print(person)


# Access values
print(person["name"])
print(person["age"])


# Get a value
print(person.get("city"))


# Missing key with default
print(person.get("country", "Unknown"))


# Change value
person["age"] = 21

print(person)


# Add value
person["country"] = "India"

print(person)


# Loop through keys
for key in person:
    print(key)


# Loop through values
for value in person.values():
    print(value)


# Loop through keys and values
for key, value in person.items():
    print(key, value)


# Dictionary methods
print(person.keys())
print(person.values())
print(person.items())


# Update dictionary
person.update({
    "age": 22,
    "job": "Developer"
})

print(person)


# Remove value
person.pop("job")

print(person)


# --------------------
# SETS
# --------------------

# Create a set
numbers = {1, 2, 3, 4}

print(numbers)


# Duplicate values are removed
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)


# Add value
numbers.add(4)

print(numbers)


# Remove value
numbers.remove(2)

print(numbers)


# Discard value
numbers.discard(100)

print(numbers)


# Membership
print(3 in numbers)


# Loop through set
for number in numbers:
    print(number)


# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)


# Method versions
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# --------------------
# CHOOSING STRUCTURES
# --------------------

# List for changeable items
shopping_cart = ["bread", "milk"]

shopping_cart.append("eggs")

print(shopping_cart)


# Tuple for fixed values
coordinates = (10, 20)

print(coordinates)


# Dictionary for labeled data
student = {
    "name": "Alex",
    "age": 20,
    "score": 95
}

print(student["name"])
print(student["score"])


# Set for unique values
users = {"alex", "john", "alex", "sam"}

print(users)


# --------------------
# USER INPUT EXAMPLE
# --------------------

names = []

for i in range(3):
    name = input("Enter a name: ").strip()
    names.append(name)

print(names)


# Remove duplicates
unique_names = set(names)

print(unique_names)


# Student dictionary
student = {}

student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: "))
student["score"] = float(input("Enter student score: "))

print(student)


# Display student data
for key, value in student.items():
    print(f"{key}: {value}")
