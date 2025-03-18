import pickle

from AddressBook import AddressBook, Record

from .input_err import input_error
from .get_upcoming_birthdays import get_upcoming_birthdays


@input_error
def add_contact(args:list, book: AddressBook)->str:
   
    if  not len(args) or len(args) != 2:
        raise ValueError("Please add all arguments: contact name and phone number for this command.")     
        
    name, phone, *_ = args
    record = book.find(name)
    message = f"Contact {name.capitalize()} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name.capitalize()} added."
    if phone:
        record.add_phone(phone)        
            
    return message

@input_error
def change_phone(args:list,book: AddressBook)->str:
    if not len(args) or len(args) != 3:
        raise ValueError("Please add all arguments: contact name, old phone number and new phone number for this command.")    
      
    name,old_phone,new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    record.edit_phone(old_phone,new_phone)
    return f"Contact {name.capitalize()} updated."

   

@input_error
def show_all(book: AddressBook)->str:
    contacts = book.all_records()   
    if not len(contacts):
        return "List is empty.Please add contacts"   

    return contacts
  

@input_error
def show_phone(args:list,book: AddressBook)->str:
    if not len(args) or len(args) != 1:
        raise ValueError("Please add all arguments: contact name for this command.")    
      
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    return str(record)
    
@input_error
def add_birthday(args, book: AddressBook):
    if not len(args) or len(args) != 2:
        raise ValueError("Please add all arguments: name of user for this command.")
    name,birthday,*_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    record.add_birthday(birthday)
    return f"Birthday date to contact {name.capitalize()} added."

    
@input_error
def show_birthday(args, book: AddressBook)->str:
    if not len(args):
        raise ValueError("Please add all arguments: name of user for this command.")    
      
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Please enter a valid name of contact.")
    birthday = record.show_birthday()
    if birthday is None:
        return f"Birthday date for contact {name.capitalize()} is not added."
    return f"Birthday date for contact {name.capitalize()} is {birthday}."

    
@input_error  
def show_upcoming_birthdays( book: AddressBook)->str:
    upcoming_birthdays = book.get_upcoming_birthdays()   
    result = get_upcoming_birthdays(upcoming_birthdays)
    if  not len(result):
        return "No birthdays in next week."    
    return result

def save_data(book:AddressBook, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 