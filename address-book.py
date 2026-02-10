"""
CLI address book application.

Stores contacts with a first name, last name, phone number, email address,
and an optional note. Provides options to add, list, search, and delete contacts.
"""

class Contact:
    """
    Represent a single contact entry.

    Attributes
    ----------
    first_name : str
        Contact's first name.
    last_name : str
        Contact's last name.
    number : int
        Contact's phone number.
    email : str
        Contact's email address.
    note : str
        Optional note about the contact.
    """
    def __init__(self, first_name, last_name, number, email, note):
        """
        Initialize a Contact instance.

        Parameters
        ----------
        first_name : str
            Contact's first name.
        last_name : str
            Contact's last name.
        number : int
            Contact's phone number.
        email : str
            Contact's email address.
        note : str
            Optional note about the contact.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.note = note
        
        
    def format_contacts(self,contact):
        """
        Format a list of contacts as a multi-line string.

        Notes
        -----
        This method does not sort the contacts; it only formats them.

        Parameters
        ----------
        contacts : list[Contact]
            A list of Contact objects to format.

        Returns
        -------
        str
            A formatted string where each contact is on its own line.
        """
        formating_result = []
        contact_number = 1
        for c in contact:
            formating_result.append(
                f"{contact_number} | First name: {c.first_name} | Last name: {c.last_name}"
                f"| Phone number: {c.number} | Email: {c.email} | Note: {c.note}")
            contact_number += 1
        return "\n".join(formating_result)

class Address_book:
    """
    Manage contacts in an address book.

    Provides basic operations to add, list, search, and delete contacts
    via a command-line interface.
    """        
    def __init__(self):
        """
        Initialize the address book with an empty contact list.
        """
        self.contact_list = []
        

    def add_contact(self):
        """
        Add a new contact to the address book via user input.

        Returns
        -------
        str
            A status message indicating whether the contact was saved or an error occurred.
        """
        
        first_name = input("Enter the first name:")
        last_name = input("Enter the last name:")
        
        if len(first_name and last_name) == 0:
            return "First name and last name cannot be empty!❌" 
        
        number = int(input("Enter the number:"))
        email = input("Enter the Email address:")
        note = input("Enter the note:")
        
        contact = Contact(first_name, last_name, number, email, note)
        self.contact_list.append(contact)
        return "Contact saved✅"
    
    
    def show_contact(self):
        """
        Display all contacts in the address book.

        Returns
        -------
        str
            A formatted list of contacts, or an error message if 
            the address book is empty.
        """
        if len(self.contact_list) == 0:
            return "The address book is empty!❌"
        else:
            return Contact.format_contacts(self, self.contact_list)
        
        
    def search_contact(self):
        """
        Search contacts by first name or last name via user input.

        Notes
        -----
        This method updates `self.found_list` with matched Contact objects.

        Returns
        -------
        str
            A formatted list of matched contacts, or a "not found" message.
        """
        # keep the last search results for delete-by-search workflow.
        self.found_list = []
        query = input("Please enter a first name or last name to search:"
                      ).lower().strip()
        
        for search in self.contact_list:
            if search.first_name.lower().strip() == query or search.last_name.lower().strip() == query:
                self.found_list.append(search)
                
        if len(self.found_list) > 0:
            return Contact.format_contacts(self, self.found_list)
        else:
            return f"Contact not found!❌"     
          
            
    def delete_contact(self):
        """
        Delete a contact selected by the user.

        The user can choose to delete from:
        1) all contacts, or
        2) the most recent search results (stored in `self.found_list`).

        Returns
        -------
        str
            A confirmation message including the deleted contact's name.
        """
        delete_option = input("Please select a contact display option:"
                              "\n1) Show all contacts."
                              "\n2) Search contacts by first name or last name."
                              ).lower().strip()
        
        if delete_option == "1" or delete_option == "showallcontacts":
            print(self.show_contact())
            delete_contact_number = int(input("Please select the number of "
                                              "the contact you want:"))
            delete_contact_number -= 1
            deletet_contact = self.contact_list.pop(delete_contact_number)
            return (f"First name: {deletet_contact.first_name}"
                   f" | Last name: {deletet_contact.last_name}"
                   f" deleted successfully✅")
                    
        elif (delete_option == "2" or delete_option == "firstname" 
        or delete_option == "lastname"):
            print(self.search_contact())
            delete_contact_number = int(input("Please select the number of the"
                                              " contact you want:"))
            delete_contact_number -= 1
            deletet_contact = self.found_list[delete_contact_number]
            self.contact_list.remove(deletet_contact)
        return (f"First name: {deletet_contact.first_name}"
                f" | Last name: {deletet_contact.last_name} deleted successfully✅")
            
        
    def exit_program(self):
        """
        Signal the main loop to stop.

        Returns
        -------
        bool
            Always returns False to stop the main loop.
        """
        return False
        
        
# ----------------------------------------------------------------------
# MAIN PROGRAM EXECUTION BLOCK
# ----------------------------------------------------------------------    
        
        
operation = Address_book()    
start_program = True    
while start_program:
    print('\n☎️Address book☎️')
    print('1) Add contact')
    print('2) View all contacts')
    print('3) Search contact')
    print('4) Delete contact')
    print('5) Exit')
    
    # User menu selection
    choice_number = int(input('Choice: '))
    
    # Menu routing
    if choice_number == 1:
        print(operation.add_contact())
        
    elif choice_number == 2:
        print(operation.show_contact())
        
    elif choice_number == 3:
        print(operation.search_contact())
        
    elif choice_number == 4:
        print(operation.delete_contact())
        
    elif choice_number == 5:
        print('Exit. Goodbye!')
        start_program = operation.exit_program()
        
    else:
        print('Invalid selection. Please enter a number between 1 and 5.')