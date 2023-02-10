# Program: Phonebook using OOP
# Description:
#   - Contact.name will store the name
#   - Contact.number will store 10-digit phone number
#   - Phonebook.contacts stores a list of Contact objects.

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        new_contact = Contact(name, number)
        self.contacts.append(new_contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)


phonebook = Phonebook()

while True:
    print()
    print("1. Add contact")
    print("2. Find contact")
    print("3. Delete contact")
    print("4. Print contacts")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        phonebook.add_contact(name, number)
    elif choice == 2:
        name = input("Enter the name: ")
        contact = phonebook.find_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found.")
    elif choice == 3:
        name = input("Enter the name: ")
        phonebook.delete_contact(name)
    elif choice == 4:
        phonebook.print_contacts()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
