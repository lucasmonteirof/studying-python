from src.age_calculator import AgeCalculator
import datetime

def test_calculate_age():
    assert AgeCalculator.calculate_age(datetime.date(1994, 10, 19)) == 30
    assert AgeCalculator.calculate_age(datetime.date(2004, 8, 25)) == 20
