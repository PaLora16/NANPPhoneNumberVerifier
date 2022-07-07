'''
Running tests:
1. Install inti venv pytest (pip install pytest)
2. cd to test_clean.py folder
3. from console run :  pytest -v
'''


from clean import VerifyNANPPhoneNumber
import pytest

test__data = [
    "+1 (613)-995-0253",
    "613-995-0253",
    "1 613 995 0253",
    "613.995.0253"

]


def test_verify_phone_number():
    for phone in test__data:
        phone = VerifyNANPPhoneNumber().validate(phone)
        assert phone == '6139950253'


def test_more_than_eleven_digits():
    with pytest.raises(ValueError, match="more than 11 digits"):
        VerifyNANPPhoneNumber().validate("1 613 995 0253487")


def test_incorrect_number_of_digits():
    with pytest.raises(ValueError, match="incorrect number of digits"):
        VerifyNANPPhoneNumber().validate("1 613 995 02")


def test_must_start_with_one_if_eleven_numbers():
    with pytest.raises(ValueError, match="must start with 1"):
        VerifyNANPPhoneNumber().validate("0 613 995 0253")


def test_no_letters_allowed():
    with pytest.raises(ValueError, match='letters not permitted'):
        VerifyNANPPhoneNumber().validate("0 N13 995 0253")


def test_punctuations_not_permitted():
    with pytest.raises(ValueError, match='punctuations not permitted'):
        VerifyNANPPhoneNumber().validate("613-995-102-3")


def test_exchange_code_cannot_start_with_zero():
    with pytest.raises(ValueError, match='exchange code cannot start with zero'):
        VerifyNANPPhoneNumber().validate("1 613 095 0253")

def test_exchange_code_cannot_start_with_one():
    with pytest.raises(ValueError, match='exchange code cannot start with one'):
        VerifyNANPPhoneNumber().validate("1 613 195 0253")

def test_area_code_cannot_start_with_one():
    with pytest.raises(ValueError, match='area code cannot start with one'):
        VerifyNANPPhoneNumber().validate("1 113 795 0253")
def test_area_code_cannot_start_with_zero():
    with pytest.raises(ValueError, match='area code cannot start with zero'):
        VerifyNANPPhoneNumber().validate("1 013 795 0253")
