import datetime

class AgeCalculator:
    def calculate_age(date_of_birth, comparison_date=datetime.date.today()):
        age = comparison_date.year - date_of_birth.year
        
        if (comparison_date.month, comparison_date.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1

        return age
