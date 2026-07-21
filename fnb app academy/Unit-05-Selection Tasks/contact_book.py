contacts = []

def add_contact():
    print(" Add Contact ")

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact added successfully!")


def search_contact(name):

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None


def delete_contact(name):

    contact = search_contact(name)

    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def view_all():

    if len(contacts) == 0:
        print("No contacts found.")
        return

    print(" CONTACT LIST ")

    for contact in contacts:
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


while True:

    print(" CONTACT BOOK ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":

        name = input("Enter contact name to search: ")

        result = search_contact(name)

        if result:
            print("Contact Found")
            print(f"Name : {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":

        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")