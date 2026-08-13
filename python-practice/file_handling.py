# FILES


# --------------------
# WRITING A TEXT FILE
# --------------------

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("I am learning files\n")
    file.write("This is a text file")


# --------------------
# READING A TEXT FILE
# --------------------

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


# --------------------
# READING ONE LINE
# --------------------

with open("example.txt", "r", encoding="utf-8") as file:
    line = file.readline()

print(line)


# --------------------
# READING ALL LINES
# --------------------

with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)


# --------------------
# LOOP THROUGH FILE
# --------------------

with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# --------------------
# APPENDING
# --------------------

with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line added")


# --------------------
# READ AFTER APPENDING
# --------------------

with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())


# --------------------
# HANDLE MISSING FILE
# --------------------

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found")


# --------------------
# CSV WRITING
# --------------------

import csv

with open("students.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alex", 20, "Delhi"])
    writer.writerow(["Sam", 22, "Mumbai"])


# --------------------
# CSV READING
# --------------------

with open("students.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# --------------------
# CSV DICTIONARIES
# --------------------

with open("students.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
        print(row["age"])
        print(row["city"])


# --------------------
# CSV DICTIONARY WRITING
# --------------------

with open("students2.csv", "w", newline="", encoding="utf-8") as file:

    fieldnames = ["name", "age", "city"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "name": "Alex",
        "age": 20,
        "city": "Delhi"
    })

    writer.writerow({
        "name": "Sam",
        "age": 22,
        "city": "Mumbai"
    })


# --------------------
# JSON WRITING
# --------------------

import json

student = {
    "name": "Alex",
    "age": 20,
    "city": "Delhi"
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)


# --------------------
# JSON READING
# --------------------

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)


# Access JSON data
print(student["name"])
print(student["age"])


# --------------------
# JSON WITH LISTS
# --------------------

students = [
    {
        "name": "Alex",
        "age": 20
    },
    {
        "name": "Sam",
        "age": 22
    }
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)


# Read JSON list
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print(student["name"])


# --------------------
# JSON STRING
# --------------------

student = {
    "name": "Alex",
    "age": 20
}

json_text = json.dumps(student)

print(json_text)


# Convert JSON string back
student = json.loads(json_text)

print(student["name"])


# --------------------
# SIMPLE FILE PROJECT
# --------------------

name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")


# Read saved information
with open("user.txt", "r", encoding="utf-8") as file:
    saved_data = file.read()

print(saved_data)
