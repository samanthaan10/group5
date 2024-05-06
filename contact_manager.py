import re
import difflib

class User:
    """
    This class represents a user in the contact management system.

    Attributes:
        user_id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        phone_number (str): The phone number of the user.
        contacts (list): A list of Contact objects associated with the user.
    """
    
    def __init__(self, user_id=None, username=None, email=None, phone_number=None, contacts=None):
        """
        This method initializes a User instance.

        Parameters:
            user_id (int, optional): The unique identifier for the user.
            username (str, optional): The username of the user.
            email (str, optional): The email address of the user.
            phone_number (str, optional): The phone number of the user.
            contacts (list, optional): A list of Contact objects associated with the user.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.contacts = contacts if contacts is not None else []

    def add_contact(self, name, phone_number, email):
        """
        This method adds a contact to the user's contact list.

        Parameters:
            name (str): The name of the contact.
            phone_number (str): The phone number of the contact.
            email (str): The email address of the contact.
        """
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
        

    def delete_contact(self, name):
        """
        This method deletes a contact from the user's contact list.

        Parameters:
            name (str): The name of the contact to be deleted.
        """
        deleted = False
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                deleted = True
        if not deleted:
            print("Contact not found.")
        
  
    def search_contacts(self, query):
        """
        This method searches for contacts whose names contain the specified query.

        Parameters:
            query (str): The search query to match against contact names.
        """
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower()]
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(contact.name)  # Print the contact's name directly
        else:
            print("No contacts found.")

    def display_contacts(self):
        """
        This method displays all contacts of the user.
        """
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts found.")

class Contact:
    """
    This method represents an individual contact.

    Attributes:
        name (str): The name of the contact.
        phone_number (str): The phone number of the contact.
        email (str): The email address of the contact.
    """

    def __init__(self, name, phone_number, email):
        """
        This method initializes a Contact instance.

        Parameters:
            name (str): The name of the contact.
            phone_number (str): The phone number of the contact.
            email (str): The email address of the contact.
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_name(self):
        """
        This method gets the name of the contact.

        Returns:
            str: The name of the contact.
        """
        return self.name

    def get_number(self):
        """
        This method gets the phone number of the contact.

        Returns:
            str: The phone number of the contact.
        """
        return self.phone_number

    def set_email(self, email):
        """
        This method sets the email address of the contact.

        Parameters:
            email (str): The email address to set.
        """
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        self.email = email

    def get_email(self):
        """
        This method gets the email address of the contact.

        Returns:
            str: The email address of the contact.
        """
        return self.email

def main():
    """
    The main function to run the contact management system.
    """
    user_id = 1
    username = "example_user"
    email = "example@example.com"
    phone_number = "1234567890"
    user = User(user_id, username, email, phone_number)

    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            if not name.strip().replace(" ", "").isalpha():  # Check if name contains only letters and spaces
                print("Invalid input for contact name.")
                continue

            phone_number = input("Enter contact phone number: ")
            if not phone_number.strip().replace(" ", "").isdigit():  # Check if phone number contains only digits and spaces
                print("Invalid input for phone number.")
                continue

            email = input("Enter contact email: ")
            try:
                user.add_contact(name, phone_number, email)
            except ValueError as e:
                print(e)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            user.delete_contact(name)
        elif choice == "3":
            query = input("Enter search keyword: ")
            user.search_contacts(query)
        elif choice == "4":
            user.display_contacts()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
