
import re
import string

test__data = [
    "+1 (613)-995-0253",
    "613-995-0253",
    "1 613 995 0253",
    "613.995.0253"
]

# Checking for the pattern of the phone
# Based on exercise https://exercism.org/tracks/python/exercises/phone-number


class VerifyNANPPhoneNumber():
    """
    Verify and normalize NANP phone number
    """

    def __str__(self):
        return self._phone_number

    def _remove_punctuation(self, chunk: str) -> str:
        # Cleans up punctuation (if any) from phone number chunk
        return ''.join(c for c in chunk if c not in string.punctuation)

    def _split_phone_number_and_remove_punctuation(self, phone_number: str) -> list[str]:
        # split into chunk of seqeunces according to -. space separators
        _splitted = re.split('[-.\s]', phone_number)
        # filter out country code if any and remove punctuation
        return [self._remove_punctuation(s) for s in _splitted if len(s) >= 3]

    def _get_numbers_count(self, phone_number: str) -> int:
        # count of digits in phone
        return len(self._get_just_numbers(phone_number))

    def _get_just_numbers(self, phone_number: str) -> list[str]:
        # pick up just numbers
        return [c for c in phone_number if (c in '0123456789')]

    def _check_numbers_count(self, phone_number: str) -> None:
        i = self._get_numbers_count(phone_number)
        if i > 11:
            raise ValueError("more than 11 digits")
        if i < 10:
            raise ValueError("incorrect number of digits")

    def _check_start_with_one_if_eleven_numbers(self, phone_number: str) -> None:
        if self._get_numbers_count(phone_number) == 11 and self._get_just_numbers(phone_number)[0] != '1':
            raise ValueError("must start with 1")

    def _check_if_letters(self, phone_number: str) -> None:
        '''Check if argument contain letters'''
        if any(c.isalpha() for c in phone_number):
            raise ValueError("letters not permitted")

    # if punctuation inside phone number, then actual shape is not nornalized
    # expected normalized phone number shape ['xxx','xxx','xxxx'] where x = <0..9>
    def _check_punctuation(self, normalized_phone_number: list[str]) -> None:
        '''Check pattern 0..9'''
        if (len(normalized_phone_number) == 3):
            helper_tuple = (bool(re.match(r'\d{3}', normalized_phone_number[0])),
                            bool(
                re.match(r'\d{3}', normalized_phone_number[1])),
                bool(re.match(r'\d{4}', normalized_phone_number[2])))
            if all(helper_tuple):
                return
        raise ValueError("punctuations not permitted")

    def _check_exchange_code(self, exchange: str) -> None:
        if exchange.startswith('0'):
            raise ValueError("exchange code cannot start with zero")
        if exchange.startswith('1'):
            raise ValueError("exchange code cannot start with one")

    def _check_area_code(self, area: str) -> None:
        if area.startswith('0'):
            raise ValueError("area code cannot start with zero")
        if area.startswith('1'):
            raise ValueError("area code cannot start with one")

    def validate(self, phone_number: str) -> str:
        self._check_if_letters(phone_number)
        self._check_numbers_count(phone_number)
        self._check_start_with_one_if_eleven_numbers(phone_number)
        _normalized_phone_number = self._split_phone_number_and_remove_punctuation(
            phone_number)
        self._check_punctuation(_normalized_phone_number)
        self._check_area_code(_normalized_phone_number[0])
        self._check_exchange_code(_normalized_phone_number[1])
        return ''.join(_normalized_phone_number)


if __name__ == '__main__':
    for data in test__data:
        phone = VerifyNANPPhoneNumber().validate(data)
        print(phone)
