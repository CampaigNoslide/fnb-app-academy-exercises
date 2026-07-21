firstName = input("Enter your first name: ").strip()
lastName = input("Enter your last name: ").strip()
bio = input("Write a short bio (1 sentence): ").strip()

username = (firstName[0] + lastName).lower()

length_bio = len(bio)

bio = bio.replace("I am", "I'm")

print(f"Title Case: {(firstName + ' ' + lastName).title()}")
print(f"Username: {username}")
print(f"Bio: {bio}")
print(f"The number of characters in your bio is {length_bio}")