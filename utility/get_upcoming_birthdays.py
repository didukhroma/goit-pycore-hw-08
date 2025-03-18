from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list)->list:

    result = []
    today = datetime.now().date()    
    next_week = today + timedelta(days=7)

    for user in users:
        
        converted_birthday = datetime.strptime(user["birthday"],"%d.%m.%Y")        

        birthday_this_year = datetime(year=today.year  , month=converted_birthday.month, day=converted_birthday.day).date()
                
        birthday = datetime(year=today.year+1 if birthday_this_year < today else today.year, month=converted_birthday.month, day=converted_birthday.day).date() 

        congratulation_date = datetime(year=birthday.year, month=birthday.month, day=birthday.day).date() if birthday.weekday() <5 else birthday + timedelta(days=7-birthday.weekday())
       
      
        if today.toordinal() <=  congratulation_date.toordinal() <= next_week.toordinal():  
          
            user_data={'name': user['name'], 'congratulation_date':  congratulation_date.strftime("%d.%m.%Y")}
            result.append(user_data) 

    return result