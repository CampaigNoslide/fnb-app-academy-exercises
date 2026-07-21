print(" Feul Cost Calculator ")

km = float(input("Enter kilometers you will drive: "))
feulPrice = float(input("Enter feul price per liter: "))

print("since the car uses 1 Liter for every 10 Kilometer")

liters_needed = km / 10
totalFeulPrice = liters_needed * feulPrice

print(f"the total feul cost for your trip is R{ round(totalFeulPrice,2)} ")