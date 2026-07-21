contacts = {
    "John": "0821112222",
    "Mary": "0733334444",
    "Peter": "0715556666"
}

friend = input("Enter the name of the friend you want to look up: ")

if friend in contacts:
    print(f"Found! {friend}'s number is {contacts[friend]}")
else:
    print("Contact not found.")