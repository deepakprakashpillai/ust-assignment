phonebook = {}

def add_contact(name, phone_number, email=None):
    phonebook[name] = {"phone_number": phone_number, "email": email}

def search_contact(name):
    if name in phonebook:
        contact = phonebook[name]
        print(f"Name: {name}, Phone: {contact['phone_number']}, Email: {contact.get('email', 'Not available')}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(name, phone_number=None, email=None):
    if name in phonebook:
        if phone_number:
            phonebook[name]['phone_number'] = phone_number
        if email:
            phonebook[name]['email'] = email
    else:
        print(f"Contact '{name}' not found.")

def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    for name, info in phonebook.items():
        print(f"Name: {name}, Phone: {info['phone_number']}, Email: {info.get('email', 'Not available')}")

add_contact("Alice", "1234567890", "alice@example.com")
add_contact("Bob", "9876543210")
add_contact("Charlie", "5678901234", "charlie@example.com")

display_contacts()
print("---------------------------------------------------------------------------------------------------------------------------------------------")
search_contact("Alice")
print("---------------------------------------------------------------------------------------------------------------------------------------------")

update_contact("Bob", phone_number="9999999999", email="bob@example.com")

remove_contact("Charlie")

display_contacts()
