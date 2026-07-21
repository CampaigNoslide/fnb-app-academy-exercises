firstname = input("Enter your first name: ")
mark1 = float(input("Enter your first mark: "))
mark2 = float(input("Enter your second mark: "))
mark3 = float(input("Enter your third mark: "))

avg = round((mark1 + mark2 + mark3) / 3,2)

if avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else :
    grade = "F"

if avg >= 50:
    result = "Pass"
else:
    result = "Fail"

if mark1 < 40 :
    msg = "mark 1 needs intervention"

if mark2 < 40 :
    msg = "mark 2 needs intervention"

if mark3 < 40 :
    msg = "mark 3 needs intervention"


print(" Grade Classifer ")
print(f" Name: {firstname}")
print(f" Mark 1:  {mark1}")
print(f" Mark 2:  {mark2}")
print(f" Mark 3:  {mark3}")
print(f" Average: {avg} ")
print(f" Grade:  {grade}")
print(f" Result:  {result}")
print(f"Intervention:  {msg}")