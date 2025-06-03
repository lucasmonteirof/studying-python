from src.age_calculator import AgeCalculator
import datetime

def test_calculate_age():
    fixed_date = datetime.date(2025, 5, 31)
    assert AgeCalculator.calculate_age(datetime.date(1994, 10, 19), fixed_date) == 30
    assert AgeCalculator.calculate_age(datetime.date(2004, 8, 25), fixed_date) == 20
