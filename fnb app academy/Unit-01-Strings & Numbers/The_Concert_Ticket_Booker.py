sold = 0
ticket = 5
    
while sold < ticket:
    fullName = input("Enter your full name : ")
    artist = input("Enter artist name band/artist you want to see : ")

    print(f"Hey {fullName} your ticket to see {artist} is booked successfully .")

    sold =+1

    print(f" ticket sold {sold}")
    print(f" ticket remanining {ticket - sold}")
print(f"Sorry all tickets are sold out !!!")




