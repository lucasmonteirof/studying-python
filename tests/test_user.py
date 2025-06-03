from src.models.user import User
import datetime

def test_user_init():
    user = User("Lucas", datetime.date(1994, 10, 19))

    assert user.full_name == "Lucas"
    assert user.date_of_birth == datetime.date(1994, 10, 19)
