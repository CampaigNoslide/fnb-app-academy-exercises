students = [
    {"name": "Sipho", "maths": 75, "english": 80, "science": 90},
    {"name": "Mpho", "maths": 65, "english": 70, "science": 60},
    {"name": "Thabiso", "maths": 45, "english": 50, "science": 55},
    {"name": "Sarah", "maths": 95, "english": 90, "science": 92},
    {"name": "Mandla", "maths": 30, "english": 40, "science": 35}
]

results = []

total_average = 0
Max_average = 0
Min_average = 100

for student in students:

    average = round((student["maths"] + student["english"] + student["science"]) / 3, 2)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    total_average += average

    if average > Max_average:
        Max_average = average

    if average < Min_average:
        Min_average = average


class_average = round(total_average / len(students), 2)

print(" CLASS REPORT ")

for student in results:
    print(f"Name    : {student['name']}")
    print(f"Average : {student['average']}")
    print(f"Grade   : {student['grade']}")
    print(f"Status  : {student['status']}")

print("CLASS STATISTICS ")
print(f"Class Average : {class_average}")
print(f"Highest Average : {Max_average}")
print(f"Lowest Average : {Min_average}")

while True:

    search = input("Enter a student name to search (or type 'exit'): ").strip()

    if search.lower() == "exit":
        print("Program closed.")
        break

    found = False

    for student in results:

        if student["name"].lower() == search.lower():

            print("Student Found")
            print(f"Name    : {student['name']}")
            print(f"Average : {student['average']}")
            print(f"Grade   : {student['grade']}")
            print(f"Status  : {student['status']}")

            found = True
            break

    if not found:
        print("Student not found.")