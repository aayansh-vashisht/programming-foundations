import json
import os

DATA_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts(filepath=DATA_FILE):
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

# Save contacts dictionary to JSON file
def save_contacts(contacts, filepath=DATA_FILE):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contacts[name] = {
        "phone": phone if phone else "N/A",
        "email": email if email else "N/A"
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

# Search contacts by partial or full name
def search_contact(contacts):
    query = input("Enter name to search: ").strip().lower()
    matches = {name: info for name, info in contacts.items() if query in name.lower()}

    if not matches:
        print(f"No contacts matching '{query}' found.")
        return

    print(f"\nFound {len(matches)} matching contact(s):")
    for name, info in matches.items():
        print(f"- {name} | Phone: {info.get('phone')} | Email: {info.get('email')}")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' does not exist.")
        return

    print(f"Editing '{name}'. Leave blank to keep current value.")
    new_phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    new_email = input(f"New email [{contacts[name]['email']}]: ").strip()

    if new_phone:
        contacts[name]["phone"] = new_phone
    if new_email:
        contacts[name]["email"] = new_email

    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully.")

# Delete an existing contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' does not exist.")
        return

    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully.")

# List all stored contacts
def list_contacts(contacts):
    if not contacts:
        print("No contacts found. Your contact list is empty.")
        return

    print("\n--- Saved Contacts ---")
    for name, info in sorted(contacts.items()):
        print(f"- {name} | Phone: {info.get('phone')} | Email: {info.get('email')}")
    print("----------------------")

# Interactive menu loop
def main():
    contacts = load_contacts()

    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. List all contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 6.")

if __name__ == "__main__":
    main()
