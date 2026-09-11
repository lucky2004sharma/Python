contacts = {}

while True:
    name = input("\nEnter name (or done): ")

    if name == "done":
        break

    phone = input("Enter phone: ")

    contacts[name] = phone

print("\nContacts:")

for name, phone in contacts.items():
    print(name, ":", phone)