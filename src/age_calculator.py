import datetime

class AgeCalculator:
    def calculate_age(date_of_birth):
        today = datetime.date.today()
        age = today.year - date_of_birth.year
        
        if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1

        return age
