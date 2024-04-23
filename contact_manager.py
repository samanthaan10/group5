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
def __init__(self, user_id, username, email, phone_number, contacts):
       self.user_id = user_id
       self.username = username
       self.email = email
       self.phone_number = phone_number
       self.contacts =  contacts
def add_contact(self, name, phone_number, email):
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

Class Contact:
"""A class for individual contacts

  Attributes: 
        name (str): The name of the contact
        phone_number (str): The phone number for the contact
        email (str): The email address for the contact
"""
def __init__(self, name, phone_number, email):
       self.name = name
       self.phone_numner = phone_numner
       self.email = email
       

def database(): 
  """Represents a database with all of the contacts

  Attributes: 
    id (tuple): The name, number, and email of one contact 
    contact (dictionary): a dictionary of all the ids 
  """
def get_name(self):
 """grabs the name of the contact

  Returns:
   str: the name of the contact
  """
  return.self.name # returning the name of the contact

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
  """Takes the username and password of person logging in and displays address book if username and password are correct
  Parameters:
    username (str)
      username of the person logging in
    password (str)
      password that matches with the username 

  Returns:
      - if username and password are correct return:
            address_book
              completely organized/managed address book of the user
      - else return:
        None
  """
