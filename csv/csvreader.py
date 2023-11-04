import csv

def csvwrite():
    name = input("Whats the name? ")
    home = input("Whats the home? ")

    with open("csv/harryporter.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home}) 

csvwrite()

def csvreader():
    students = []

    with open("csv/students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["Name"], "age": row["Age"], "email": row["Email"]})

    for student in sorted(students, key=lambda student: student["age"]):
        print(f"{student['name']} is {student['age']} years old ")