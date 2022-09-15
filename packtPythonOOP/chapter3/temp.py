class ContactList(list):
    def firstname_search(self, firstname):
        """Add search functionality to built-in list class"""
        self.contacts_found = []
        for contact in self:
            if firstname.lower() in contact.firstname.lower():
                self.contacts_found.append(contact)
        return self.contacts_found


class Contacts:
    """Lets create a contacts class!"""

    contacts_list = ContactList()

    def __init__(self, firstname, lastname, email=""):
        """initialize a contact with base informattion"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        Contacts.contacts_list.append(self)

    def search_contact(self, firstname):
        """firstname search on list of contacts"""
        return [contact.name for contact in self.contacts_list.firstname_search(firstname)]
