#Unit Tests for Contact Manager

    def test_delete_contact_existing(self): 
        self.user = User("Jen")
        self.user.add_contact("John", "7814676223", "john@gmail.com")
        self.user.add_contact("James", "6172463758", "james@icloud.com")
        
    def test_delete_contact_nonexistent(self): 
        self.user.delete_contact("Grace")
        self.assertEqual(len(self.user.contacts), 2)
        
    def test_valid_email(self):
        contact = Contact("Maddy", "7817389234", "maddy@gmail.com")
        self.assertEqual(contact.get_email(), "maddy@gmail.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Contact("Lauren", "2579837837", "invalid_email")
