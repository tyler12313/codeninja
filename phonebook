class Contact:
    def __init__(self, first_name, last_name, nickname, phone, secret):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.phone = phone
        self.secret = secret

    def show_details(self):
        
        print(f"{self.first_name:<12} {self.last_name} is a contact.\n its nickname is {self.nickname}.\n its secret is {self.secret}.\n This contacts phone number is {self.phone}")

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        if len(self.contacts) < 8:
            self.contacts.append(contact)
            print (f"len is {len(self.contacts)}, added {contact.first_name}")
        else:
            answer = input("you have reached the maximum of 8 contacts in this old rusty phonebook. cancel creating this new contact or delete the oldest contact? \n y to delete oldest contact, n to cancel: ")
            if answer == "y":
                print("deleting oldest contact")   
                print(f" deleted {self.contacts.pop(0).first_name}")
                self.contacts.append(contact)
                print (f"len is {len(self.contacts)}")
            if answer == "n":
                print("no")
    def show_contacts(self):
        for i in self.contacts:
            print(f"{i.first_name:<10}|{i.last_name:<10}|{i.phone:<10}|{i.nickname:<10}|\n ___________________________________________")
            
    def get_contact(self,index):
        self.contacts[index].show_details()
        
test = Contact("donald","trump","orange","99999999","orange")
# print(test.secret)
# test.show_details()

# for i in range(8):
#     phone.add_contact(test)
#phone.add_contact(person)

phonebook = PhoneBook()

while True:
    command = input("Enter command (ADD, SEARCH, EXIT): ").strip().upper()

    if command == "ADD":
        print("Adding...")
        t_firstname = input("What is the first name of the contact?")
        t_lastname = input("What is the last name of the contact?")
        t_phone = input("What is the phone number of the contact?")
        t_nickname = input("What is thename of the contact?")
        t_secret = input("What is the secret of the contact?")
        tContact = Contact(t_firstname,t_lastname,t_nickname,t_phone,t_secret)
        phonebook.add_contact(tContact)
        
    elif command == "SEARCH":
        print("Searching...")

    elif command == "EXIT":
        print("Bye!")
        break

    else:
        print("Unknown command.")

