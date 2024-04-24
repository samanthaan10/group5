#Unit Tests for Contact Manager

import unittest
from io import StringIO
from unittest.mock import patch
from contact_manager import User, Contact


class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User(1, "Ren", "ren@example.com", "4504437890")
        self.user.add_contact("Willow", "6783455412", "willow@example.com")
        self.user.add_contact("Bob", "7843336405", "bob@gmail.com")
    
    def test_add_contact(self):
        contact_name = "Rob"
        contact_phone = "4430300210"
        contact_email = "rob@gmail.com"
        self.user.add_contact(contact_name, contact_phone, contact_email)

        self.assertEqual(len(self.contact_manager.contacts), 1)
        added_contact = self.contact_manager.contacts[0]
        self.assertEqual(added_contact.name, contact_name)
        self.assertEqual(added_contact.phone_number, contact_phone)
        self.assertEqual(added_contact.email, contact_email)

    def test_delete_contact_existing(self): 
        self.user.delete_contact("Willow")
        self.assertEqual(len(self.user.contacts), 1)
        
    def test_delete_contact_nonexistent(self): 
        self.user.delete_contact("Grace")
        self.assertEqual(len(self.user.contacts), 2)

    def test_search_contacts_found(self):
        self.user = User("Sarah")
        self.user.add_contact("Carl", "7814676223", "carl@gmail.com")
        self.user.add_contact("James", "6172463758", "james@icloud.com")

        query = "Michael"
        found_contacts = self.user.search_contacts(query)
        self.assertEqual(len(found_contacts), 1)
        self.assertEqual(found_contacts[0].name, "Michael")

    def test_search_contacts_not_found(self):
        self.user = User("Liam")
        self.user.add_contact("Kendra", "7814676223", "kendra@gmail.com")
        self.user.add_contact("Moran", "6172463758", "moran@icloud.com")

        query = "Alice"
        found_contacts = self.user.search_contacts(query)
        self.assertEqual(len(found_contacts), 0)


    def test_display_contacts(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.user.display_contacts()

            expected_output = "Contacts:\nName: Willow, Phone: 6783455412, Email: willow@example.com\n" \
                              "Name: Bob, Phone: 7843336405, Email: bob@gmail.com\n"
            self.assertEqual(fake_out.getvalue(), expected_output)
        
class TestContact(unittest.TestCase):
    
    def test_valid_email(self):
        contact = Contact("Maddy", "7817389234", "maddy@gmail.com")
        self.assertEqual(contact.get_email(), "maddy@gmail.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Contact("Lauren", "2579837837", "invalid_email")

    def test_get_name(self):
        contact = Contact("John Smith", "1234567890", "john@yahoo.com")
        self.assertEqual(contact.get_name(), "John Smith")

    def test_get_number(self):
        contact = Contact("John Smith", "2404435612", "john@yahoo.com")
        self.assertEqual(contact.get_number(), "2404435612")



if __name__ == '__main__':
    unittest.main()
