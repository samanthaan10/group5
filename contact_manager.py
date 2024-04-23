Class User:

  """
     Represents a user in the contact management system.
 
     Attributes:
     - user_id (int): The unique identifier for the user.
     - username (str): The username of the user.
     - email (str): The email address of the user.
     - phone_number (str): The phone number of the user.
     - contacts (list): A list of Contact objects associated with the user.
     """
 def __init__(self, user_id, username, email, phone_number, contacts = None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.contacts =  contacts if contacts is not None else []

 def add_contact(self, name, phone_number, email):
     """ Adds a contact from the user's list 
 
     Attributes: 
     name (str): the name of the contact that will be delted
     phone_number (int): the phone number of the contact that will be delted
     email (str): the email of the contact that will be delted
 
     """
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
 
 def delete_contact(self, name): 
     """ Deletes a contact from the user's list 
 
     Attributes: 
     name (str): the name of the contact that will be delted
 
     """
     for contact in self.contacts: 
         if contact.name == name: 
             self.contacts.remove(contact) #deleting the contact 
             break #ending if statement 
 
 def search_contacts(self, query):
     """Search for contacts whose names contain the specified query.
 
         Attributes:
             query (str): The search query.
       
    """
    found_contacts = [contact for contact in self.contacts if query.lower() in contact.get_name().lower()]
         if found_contacts:
             print("Found contacts:")
             for contact in found_contacts:
                 print(contact)
         else:
             print("No contacts found matching the query.")

Class Contact:
 """A class for individual contacts
 
   Attributes: 
         name (str): The name of the contact
         phone_number (str): The phone number for the contact
         email (str): The email address for the contact
 """
 def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
 def get_name(self):
  """grabs the name of the contact
 
   Returns:
    str: the name of the contact
   """
   return self.name # returning the name of the contact
 
  def get_number(self):
   """grabs the number of the contact
 
   Returns:
    str: the phone number of the contact
   """
   return self.phone_number # returning the phone number
  
 def set_email(self, email): 
   """set the email address of the contact 
   Arguments: 
      email(str): the email address that will be set 
         
   Returns: 
      ValueError: if the email address isnt valie 
   """
     
   if "@" not in email or "." not in email: #checking if @ is in email
       raise ValueError("Invalid email address") #if it isnt it is not a valid email address
   self.email = email
 
 def get_email(self):
   """ grabs the email address of the contact 
     
   Returns: 
       str: the email address
   """
   return self.email #returning the email address

def main ():
    user = User()
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone_number, email)
            user.add_contact(contact)
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
