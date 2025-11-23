import json
import os

class ContactBook:
    def __init__(self, filename='contacts.json'):
        """Initialize contact book with JSON file storage"""
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)
    
    def add_contact(self):
        """Add a new contact"""
        print("\n--- Add New Contact ---")
        name = input("Enter name: ").strip()
        
        if name in self.contacts:
            print(f"Contact '{name}' already exists!")
            return
        
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()
        
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        
        self.save_contacts()
        print(f"\nContact '{name}' added successfully!")
    
    def view_contacts(self):
        """Display all contacts"""
        if not self.contacts:
            print("\nNo contacts found.")
            return
        
        print("\n" + "="*60)
        print("Contact List".center(60))
        print("="*60)
        
        for name, details in self.contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print("-" * 60)
    
    def search_contact(self):
        """Search for a contact by name or phone number"""
        print("\n--- Search Contact ---")
        search_term = input("Enter name or phone number: ").strip()
        
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                print("\n" + "="*60)
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("="*60)
                found = True
        
        if not found:
            print("\nNo contact found matching your search.")
    
    def update_contact(self):
        """Update contact details"""
        print("\n--- Update Contact ---")
        name = input("Enter the name of the contact to update: ").strip()
        
        if name not in self.contacts:
            print(f"\nContact '{name}' not found!")
            return
        
        print(f"\nCurrent details for {name}:")
        print(f"Phone: {self.contacts[name]['phone']}")
        print(f"Email: {self.contacts[name]['email']}")
        print(f"Address: {self.contacts[name]['address']}")
        
        print("\nEnter new details (press Enter to keep current value):")
        phone = input("New phone number: ").strip()
        email = input("New email: ").strip()
        address = input("New address: ").strip()
        
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address
        
        self.save_contacts()
        print(f"\nContact '{name}' updated successfully!")
    
    def delete_contact(self):
        """Delete a contact"""
        print("\n--- Delete Contact ---")
        name = input("Enter the name of the contact to delete: ").strip()
        
        if name not in self.contacts:
            print(f"\nContact '{name}' not found!")
            return
        
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            del self.contacts[name]
            self.save_contacts()
            print(f"\nContact '{name}' deleted successfully!")
        else:
            print("\nDeletion cancelled.")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("Contact Book Manager".center(60))
        print("="*60)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("="*60)
    
    def run(self):
        """Main program loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("\nThank you for using Contact Book Manager!")
                break
            else:
                print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
