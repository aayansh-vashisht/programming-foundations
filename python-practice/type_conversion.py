# TYPE CONVERSION

# String to integer
age = "20"
age = int(age)

print(age)
print(type(age))


# String to float
price = "19.99"
price = float(price)

print(price)
print(type(price))


# Integer to float
number = 10
decimal_number = float(number)

print(decimal_number)


# Float to integer
number = 9.8
whole_number = int(number)

print(whole_number)


# Integer to string
age = 20
age_text = str(age)

print(age_text)
print(type(age_text))


# Number inside text
age = 20

print("I am " + str(age) + " years old")
print(f"I am {age} years old")


# Boolean conversion
print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))


# Input as integer
user_age = int(input("Enter your age: "))

print(f"In 5 years you will be {user_age + 5}")


# Input as float
height = float(input("Enter your height: "))

print(f"Your height is {height}")


# Price calculator
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total price: {total:.2f}")


# Check types
value = "100"

print(type(value))

value = int(value)

print(type(value))


# Float to int does not round
number = 9.9

print(int(number))
print(round(number))


# Decimal string
decimal_text = "10.5"

decimal_number = float(decimal_text)

print(decimal_number)

whole_number = int(decimal_number)

print(whole_number)
