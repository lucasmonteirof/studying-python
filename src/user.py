import datetime

class User:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.full_name = name
        self.date_of_birth = date_of_birth
