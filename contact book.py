class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact['name'] == name:
                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                print(f"Contact {name} updated successfully!")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print(f"Contact {name} not found.")

    def display_menu(self):
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            
            elif choice == '2':
                self.view_contacts()

            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)

            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                new_name = input("Enter new name (press enter to skip): ")
                new_phone = input("Enter new phone number (press enter to skip): ")
                new_email = input("Enter new email (press enter to skip): ")
                new_address = input("Enter new address (press enter to skip): ")
                self.update_contact(name, new_name, new_phone, new_email, new_address)

            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)

            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
