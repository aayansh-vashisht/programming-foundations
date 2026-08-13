# OBJECT-ORIENTED PROGRAMMING


# --------------------
# BASIC CLASS
# --------------------

class Student:
    pass


# Create objects
student1 = Student()
student2 = Student()

print(student1)
print(student2)


# --------------------
# ATTRIBUTES
# --------------------

student1.name = "Alex"
student1.age = 20

student2.name = "Sam"
student2.age = 22

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# --------------------
# CONSTRUCTOR
# --------------------

class Person:

    def __init__(self):
        print("Person created")


person1 = Person()
person2 = Person()


# --------------------
# CONSTRUCTOR WITH ATTRIBUTES
# --------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Alex", 20)
student2 = Student("Sam", 22)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# --------------------
# METHODS
# --------------------

class Student:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")


student1 = Student("Alex")

student1.say_hello()


# --------------------
# METHOD WITH PARAMETERS
# --------------------

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


# --------------------
# METHODS AND ATTRIBUTES
# --------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")


student1 = Student("Alex", 20)

student1.introduce()


# --------------------
# MODIFYING ATTRIBUTES
# --------------------

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(1000)

print(account.balance)

account.deposit(500)

print(account.balance)


# --------------------
# BASIC ENCAPSULATION
# --------------------

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):

        if 0 < amount <= self._balance:
            self._balance -= amount

    def show_balance(self):
        print(f"Balance: {self._balance}")


account = BankAccount(1000)

account.show_balance()

account.deposit(500)
account.show_balance()

account.withdraw(200)
account.show_balance()


# --------------------
# COMPLETE STUDENT EXAMPLE
# --------------------

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    def study(self, subject):
        print(f"{self.name} is studying {subject}")


student1 = Student("Alex", 20, "Python")

student1.introduce()
student1.study("OOP")
