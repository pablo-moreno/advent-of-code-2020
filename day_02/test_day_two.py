from unittest import TestCase
from . import DayTwo


class DayTwoTestCase(TestCase):
    def test_first_part_valid_passwords(self):
        line = '1-3 a: abcdef'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_first_part(letter, letter_range, password)

        assert result is True

        line = '2-9 c: ccccccccc'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_first_part(letter, letter_range, password)

        assert result is True

    def test_first_part_invalid_password(self):
        line = '1-3 a: cdefg'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_first_part(letter, letter_range, password)

        assert result is False

    def test_second_part_valid_password(self):
        line = '1-3 a: abcde'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_second_part(letter, letter_range, password)

        assert result is True

    def test_second_part_invalid_passwords(self):
        line = '1-3 a: cdefg'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_second_part(letter, letter_range, password)

        assert result is False

        line = '2-9 c: ccccccccc'
        letter, letter_range, password = DayTwo.parse_line(line)
        result = DayTwo.validate_password_second_part(letter, letter_range, password)

        assert result is False
