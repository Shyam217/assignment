from classes import *
from contactbook import *   
while True:
    add_contact = input("Enter \n 1 for adding contact\n 2 for deleting \n 3 for contactbook: ")
    if add_contact == "1":
        name = input("enter name: ")
        number = input("enter number: ")
        Date_of_birth= input("enter DOB: ")
        email = input("enter emial_id: ")
        address = input("enter full address: ")
        user = eachcontact(name, number,Date_of_birth, email, address )
        total_contacts += user
    elif (add_contact == "2"):
        number = input("enter number: ")
        name = input("enter name: ")
        for i in total_contacts:
            if number in i:
                index = total_contacts.index(i)
                total_contacts.pop(index)
            else:
                continue
    elif (add_contact == "3"):
        print(total_contacts)
