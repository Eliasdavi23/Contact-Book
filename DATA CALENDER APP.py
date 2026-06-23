def display_menu():
    print(
'''Menu
1. Add contact
2. View contact
3. Edit contact
4. Delete contact
5. List contact
6. Exit '''
)

def add_contact(contact_book):
    name = input("Write the contact name: ")

    if name in contact_book:
        print ("Contact already exists!")
        return
    
    phone = input("Writen the phone number: ")
    email = input("Writen the email: ")
    address = input("Writen the address: ")

    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successegully!")

def view_contact(contact_book):
    name_contact = input("Writen contact: ")

    if name_contact in contact_book:
        print(f"Name: {name_contact}")
        print(f"Phone: {contact_book[name_contact]['phone']}")
        print(f"Email: {contact_book}[name_contact]['email']")
        print(f"Address: {contact_book}[name_contact]['address']")

    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Write the contact name: ")

    if name not in contact_book:
        print("Contact not found!")
        return
    
    contact = contact_book[name]
    phone = input("Writen the phone number: ")
    email = input("Writen the email: ")
    address = input("Writen the address: ")

    if phone != "":
        contact['phone'] = phone
    if email != "":
        contact['email'] = email
    if phone != "":
        contact['address'] = address
    print("Contact updated successfully!")

def delete_contact(contact_book):
    name = input("Write the contact name: ").strip()

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfuly")
    
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contact available.")
    else:
        for name, dados in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {dados['phone']}")
            print(f"Email: {dados['email']}")
            print(f"Address: {dados['address']}")
            print("")

def main():
    contact_book = {}

    while True:
        display_menu()
        choice = input("Choice one options: ")

        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all_contacts(contact_book)
        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
main()