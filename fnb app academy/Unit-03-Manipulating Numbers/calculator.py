print(" Hy Kgomotso I am your Advanced Calculator")

number1 = float(input("Enter First Number: "  ))
number2 = float(input("Enter Second Number: " ))

print(" Enter 1 for 'Addition'") 
print("2 for 'Subtraction' ")
print("3 for 'Multiplication' ")
print("4 for 'Division'") 
print("5 for 'Modulus'")
print("6 for 'Inter Division'")
print("7 for ' Exponent' ")

operation = input("Enter Operation: ")

Total = None

if operation == "1" :
    Total = (number1 + number2)
elif operation == "2":
     Total = (number1 - number2)
elif operation == "3":
     Total = (number1 * number2)
elif operation == "4":
    if number2 == 0:
        print("Error! Division by zero is not allowed.")
    else :
         Total = (number1 / number2)
elif operation == "5":
    if number2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        Total = number1 % number2
elif operation == "6":
    if number2  == 0:
        print("Error! Division by zero is not allowed.")
    else :
         Total = (number1 // number2)
elif operation == "7":
    Total = (number1 ** number2)
else:
    print("Error! Invalid Operation")
if Total is not None:
    print(f" your total amount for the operation you choose is  {round(Total,2)}")