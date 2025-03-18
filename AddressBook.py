import re


from collections import UserDict
from dataclasses import dataclass
from datetime import datetime
from typing import Self




PHONE_PATTERN = r"\d{1}"

@dataclass
class Field():
    value:any

    def __str__(self:Self)->str:
        return str(self.value)
    
class Name(Field):
    def __init__(self:Self,name:str)->None:
        super().__init__(name)

class Phone(Field):
    def __init__(self:Self,phone:str)->None:
        self.value = phone
        self._validate()
        super().__init__(phone)

    def _validate(self:Self):
        if not re.match(PHONE_PATTERN, self.value):
            raise ValueError(f"Invalid phone number: {self.value}. Use 10 digits")
        
        

class Record():
    def __init__(self:Self,name:str)->None:
        self.name = Name(name)
        self.phones = list[Phone]() 
        self.birthday = None

    def add_phone(self:Self,phone:str)->None:
        self.phones.append(Phone(phone))

    def remove_phone(self:Self,phone:str)->None:
        self.phones.remove(Phone(phone))

    def edit_phone(self:Self,old_phone:str,new_phone:str)->None:
        index = self.phones.index(Phone(old_phone))
        self.phones[index] = Phone(new_phone)
    def find_phone(self:Self,phone:str)->str:
        return next((p.value for p in self.phones if p.value == phone), None)      

    def __str__(self:Self)->str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"   

    def add_birthday(self:Self,birthday:str)->None:
        self.birthday = BirthDay(birthday) 

    def show_birthday(self:Self):
        if self.birthday is None:
            return None
        return self.birthday.get_birthday()

class BirthDay(Field):
    def __init__(self:Self,value:str)->None:
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
            
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def get_birthday(self:Self)->str:
        return datetime.strftime(self.birthday,"%d.%m.%Y")

class AddressBook(UserDict):   

    def add_record(self:Self,record:Record)->None:
        self.data[record.name.value] = record

    def find(self:Self,name:str)->Record:
        return self.data.get(name)
    
    def delete(self:Self,name:str)->None:
        del self.data[name]

    def all_records(self:Self)->str:        
        return "\n".join(list(str(record) for record in self.data.values()))
    
    def get_upcoming_birthdays(self:Self)->list[BirthDay]:
        
        if not self.data:
            return []
            
        data = [{"name":name,"birthday":record.show_birthday()} for name,record in self.data.items() if record.show_birthday() is not None]
      
        return data


    