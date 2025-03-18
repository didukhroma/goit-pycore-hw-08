from utility import parse_input,add_contact,change_phone,show_all,show_phone,add_birthday,show_birthday,show_upcoming_birthdays,save_data,load_data
from AddressBook import AddressBook

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        
        command, args = parse_input(user_input)

        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, book))
        
        elif command == "change":
            print(change_phone(args, book))
        
        elif command == "phone":
            print(show_phone(args, book))
        
        elif command == "all":
            print(show_all(book))
        
        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        elif command == "show-birthday":
            print(show_birthday(args, book))
        
        elif command == "birthdays":
            print(show_upcoming_birthdays(book))
        
        else:
            print("Invalid command.")

    save_data(book)


if __name__ == "__main__":
    main()

