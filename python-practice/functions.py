# FUNCTIONS


# Basic function
def greet():
    print("Hello")


greet()


# Call function many times
def say_hi():
    print("Hi")


say_hi()
say_hi()


# Parameter
def greet_person(name):
    print(f"Hello {name}")


greet_person("Alex")
greet_person("John")


# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")


introduce("Alex", 20)


# Positional arguments
def subtract(a, b):
    print(a - b)


subtract(10, 3)
subtract(3, 10)


# Keyword arguments
def show_person(name, age):
    print(f"{name} is {age} years old")


show_person(age=20, name="Alex")


# Return value
def add(a, b):
    return a + b


result = add(10, 5)

print(result)


# Use returned value
def multiply(a, b):
    return a * b


result = multiply(5, 4)
answer = result + 10

print(answer)


# Square function
def square(number):
    return number ** 2


print(square(5))


# Return multiple values
def calculate(a, b):
    return a + b, a - b


total, difference = calculate(10, 5)

print(total)
print(difference)


# Default argument
def greet_guest(name="Guest"):
    print(f"Hello {name}")


greet_guest()
greet_guest("Alex")


# Default power
def power(number, exponent=2):
    return number ** exponent


print(power(5))
print(power(5, 3))


# Local scope
def local_example():
    message = "Local variable"
    print(message)


local_example()


# Global scope
name = "Alex"


def show_name():
    print(name)


show_name()


# Local and global variable
name = "Alex"


def change_name():
    name = "John"
    print(name)


change_name()
print(name)


# Change global variable
score = 10


def change_score():
    global score
    score = 20


change_score()

print(score)


# Better way with return
score = 10


def new_score():
    return 20


score = new_score()

print(score)


# Function with input
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello {name}")


greet_user()


# Pure function
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))


# Pure calculation
def calculate_total(price, quantity):
    return price * quantity


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print(f"Total: {total:.2f}")


# Boolean function
def is_adult(age):
    return age >= 18


print(is_adult(20))
print(is_adult(15))


# Use function in if
age = int(input("Enter your age: "))

if is_adult(age):
    print("Adult")
else:
    print("Under 18")


# Multiple conditions
def can_enter(age, has_ticket):
    return age >= 18 and has_ticket


print(can_enter(20, True))
print(can_enter(16, True))


# Impure function
def show_message():
    print("This changes the screen")


show_message()
