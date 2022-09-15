class ContactList(list):
    def search(self, name):
        contacts_found = []
        for contact in self:
            if name in contact.name:
                contacts_found.append(contact)
        return contacts_found


class Contacts:
    """Stores names, emails of our contacts"""

    contacts_list = ContactList()

    def __init__(self, name, email):
        """Contact initialized with name and email"""
        self.name = name
        self.email = email
        Contacts.contacts_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.email}"

    def search_contact(self, name):
        return [contact.name for contact in Contacts.contacts_list.search(name)]


class Supplier(Contacts):

    def place_order(self, order):
        self.order = order
        return f"If this was a real app. We could send {self.order} to supplier."


class Friends(Contacts):
    """inherits from Contact class and add phone number for friends."""

    def __init__(self, name, email, phone):
        """call super class init method and also add phone"""
        super().__init__(name, email)
        self.phone = phone


s = Supplier("Bilal Shahzad", "bilalshahzad@shahzadqadir.net")
c = Contacts("Hamza Shahzad", "hamzashahzad@shahzadqadir.net")

f = Friends("Hamayal Shahzad", "zunashahzad@gmail.com", '0123456')
print(c.search_contact("Shahzad"))
