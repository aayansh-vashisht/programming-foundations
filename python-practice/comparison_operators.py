# COMPARISON OPERATORS


# Equal to
a = 10
b = 10

print(a == b)


# Not equal to
a = 10
b = 5

print(a != b)


# Greater than
age = 20

print(age > 18)


# Less than
temperature = 15

print(temperature < 20)


# Greater than or equal to
age = 18

print(age >= 18)


# Less than or equal to
score = 50

print(score <= 50)


# Compare two variables
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Save comparison result
age = 20

is_adult = age >= 18

print(is_adult)


# Compare integers and floats
print(10 == 10.0)


# Number and string are different
print(10 == "10")


# Compare strings
name = "Alex"

print(name == "Alex")
print(name == "John")


# Capital letters matter
print("Python" == "python")


# Age check
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")


# Password check
password = input("Enter password: ")

if password == "python123":
    print("Correct password")
else:
    print("Wrong password")


# Yes or no check
answer = input("Enter yes or no: ").strip().lower()

if answer == "yes":
    print("You entered yes")
else:
    print("You did not enter yes")


# Compare two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Equal: {num1 == num2}")
print(f"Not equal: {num1 != num2}")
print(f"First is greater: {num1 > num2}")
print(f"First is smaller: {num1 < num2}")


# Chained comparison
number = int(input("Enter a number: "))

if 1 <= number <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")
