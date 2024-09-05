#RAMASAMY.AM
#Contact Management System

class ContactBook:
    def __init__(self):
        # Initialize an empty dictionary to store contacts
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        # Add a new contact to the dictionary
        self.contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
        print(f'Contact {name} added successfully!')

    def view_contact_list(self):
        # Display a list of all contacts with names and phone numbers
        if not self.contacts:
            print('Contact book is empty.')
        else:
            print('Contact List:')
            for name, info in self.contacts.items():
                print(f'{name}: {info["Phone Number"]}')

    def search_contact(self, search_key):
        # Search for a contact by name or phone number
        found_contacts = []
        for name, info in self.contacts.items():
            if search_key.lower() in name.lower() or search_key in info['Phone Number']:
                found_contacts.append((name, info))
        if found_contacts:
            print('Search Results:')
            for name, info in found_contacts:
                print(f'{name}: {info}')
        else:
            print('No contacts found.')

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        # Update contact details
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone_number:
                contact['Phone Number'] = new_phone_number
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            print(f'Contact {name} updated successfully!')
        else:
            print(f'Contact {name} not found in the contact book.')

    def delete_contact(self, name):
        # Delete a contact
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} deleted successfully!')
        else:
            print(f'Contact {name} not found in the contact book.')

# User Interface
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email address (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
