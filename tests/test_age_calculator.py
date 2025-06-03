from src.utils.age_calculator import AgeCalculator
import datetime
from freezegun import freeze_time

@freeze_time("2025-05-31")
def test_calculate_age():
    assert AgeCalculator.calculate_age(datetime.date(1994, 10, 19)) == 30
    assert AgeCalculator.calculate_age(datetime.date(2004, 8, 25)) == 20
