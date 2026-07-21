print(" Withdraw Simulator ")
print(" Withdrawal charges : R5.08")
print(" Deposit fee : R4.75")

Balance = 1000.50
withdrwal_fee = 5.08
Deposit_fee = 4.75
Account_Balance = 0
print(" What service are you doing today? ")
print(" 1 : Withdrwal")
print(" 2 Deposit ")

username = input("Enter your username: ")
Account_Number = input("Enter your account number: ")

operation = input("Enter the  operational service you are doing today: ")

if operation == "1" :
    withdraw = float(input("Enter the amount you want to withdraw: "))
    if withdraw <= 0:
        msg = "Invalid amount."
    elif withdraw > Balance:
        msg = "Insufficient funds."
    else:
        Account_Balance = Balance - withdraw - withdrwal_fee
        msg = f"Withdrawal successful! Remaining balance: R{Account_Balance:.2f}"
elif operation == "2":
    deposit = float(input("Enter amount to deposit: "))
    if deposit <= 0:
        msg = "Invalid deposit amount."
    else:
        Account_Balance = Balance + deposit - Deposit_fee
        msg = f"Deposit successful! New balance: R{Account_Balance:.2f}"
else:
    print(" invalid Operational number")

print(" KGOMOTSO'S ATM MACHINE ")

print("KGOMOTSO TRANSACTIONAL CHARGES")
print(f"   Withdrwal fee   :    R{withdrwal_fee}")
print(f"   Deposit fee     :    R{Deposit_fee}")
print(f"   Account Holder  :     {username}")
print(f"   Account Number  :     {Account_Number}")
print(f"Account Balance : R{Account_Balance:.2f}")
print(msg)

