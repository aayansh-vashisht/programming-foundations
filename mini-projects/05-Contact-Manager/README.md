# 📇 Contact Manager

A CLI-based contact management application built in Python that enables users to store, view, search, update, and delete contact details with JSON persistence.

---

## 🚀 Features

- ➕ **Add Contact**: Store new contact entries with name, phone number, and email.
- 📋 **List Contacts**: View all saved contacts in alphabetical order.
- 🔍 **Search**: Look up contacts using full or partial name matching.
- ✏️ **Edit Contact**: Update phone numbers or email addresses while retaining unchanged fields.
- 🗑️ **Delete Contact**: Remove unwanted contacts from storage.
- 💾 **JSON Persistence**: Automatically reads from and writes to `contacts.json` so data survives restarts.
- ⚠️ **Missing Contact Handling**: Gracefully informs the user if a queried contact does not exist without throwing errors.

---

## 📁 File Structure

```text
├── contact_manager.py   # Core contact manager application logic
├── contacts.json        # Persistent JSON storage (created automatically)
└── README.md            # Project documentation
```

---

## 🛠️ Requirements

- **Python 3.6+**
- Standard Python libraries (`json`, `os`) — *no external packages required!*

---

## 📦 How to Run

1. Navigate to the project directory:
   ```bash
   cd mini-projects/06-Contact-Manager
   ```

2. Run the application:
   ```bash
   python contact_manager.py
   ```

---

## 🖥️ Example Usage

```text
=== CONTACT MANAGER ===
1. List all contacts
2. Add contact
3. Search contact
4. Edit contact
5. Delete contact
6. Exit
Select an option (1-6): 2
Enter contact name: Jane Doe
Enter phone number: 555-0199
Enter email address: jane@example.com
Contact 'Jane Doe' added successfully.

=== CONTACT MANAGER ===
1. List all contacts
2. Add contact
3. Search contact
4. Edit contact
5. Delete contact
6. Exit
Select an option (1-6): 3
Enter name to search: jane

Found 1 matching contact(s):
- Jane Doe | Phone: 555-0199 | Email: jane@example.com
```
