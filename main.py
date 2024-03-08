from logo import logo
import Colors

print(logo)


def display_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        print("{:<15} {:<15}".format("Name", "Phone Number"))
        print("-" * 30)
        for name, number in contacts.items():
            print("{:<15} {:<15}".format(name, number))


def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number: ")
    contacts[name] = number
    print(f"{Colors.LIGHT_GREEN}Contact added successfully!{Colors.END}")


def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{Colors.LIGHT_GREEN}Contact deleted successfully!{Colors.END}")
    else:
        print(f"{Colors.LIGHT_RED}Contact not found!{Colors.END}")


def update_contact(contacts):
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        number = input("Enter the new phone number: ")
        contacts[name] = number
        print(f"{Colors.LIGHT_RED}Contact updated successfully!{Colors.END}")
    else:
        print(f"{Colors.LIGHT_RED}Contact not found!{Colors.END}")


def main():
    contacts = {}

    while True:
        print("\nClick one order")
        print("1", f"{Colors.LIGHT_GRAY}.Display Contacts")
        print("2", f"{Colors.GREEN}.Add Contact{Colors.END}")
        print("3", f"{Colors.LIGHT_RED}.Delete Contact {Colors.END}")
        print("4", f"{Colors.LIGHT_CYAN}.Update Contact{Colors.END}")
        print("5", f"{Colors.PURPLE}.Exit{Colors.END}")

        choice = input(f"{Colors.LIGHT_BLUE}Enter your choice: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print(f"{Colors.LIGHT_RED}Invalid choice! Please enter a valid option.{Colors.END}")


main()
