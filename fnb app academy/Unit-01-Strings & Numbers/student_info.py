firstName = input("Enter your first name : ")
surname = input("Enter your surname : ")
age = int(input("Enter you age : "))
favNumber = float(input("Enter your favorite number : "))

months = 12 * age
twodecimalplace = round(favNumber, 2)

print(f"Welcome  {(firstName + ' ' + surname)}")
print(firstName.upper())
print(f"Title Case: {(firstName + ' ' + surname).title()}")
print(f"You have been alive for more than {months} months")
print(f"Your favorite number is {twodecimalplace} with 2 decimal places")
print(f"firstName is a variable with the data type of {type(firstName)}")
print(f"surname is a variable with the data type of {type(surname)}")
print(f"favNumber is a variable with the data type of {type(favNumber)}")
print(f"age is a variable with the data type of {type(age)}")