from dataclasses import dataclass
import datetime

@dataclass
class User:
    full_name: str
    date_of_birth: datetime.date
