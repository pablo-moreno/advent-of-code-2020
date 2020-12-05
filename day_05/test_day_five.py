from unittest import TestCase
from . import BinaryDecoder


class DayFiveTestCase(TestCase):
    def setUp(self):
        self.boarding_codes = {
            'FBFBBFFRLR': (44, 5, 357),
            'BFFFBBFRRR': (70, 7, 567),
            'FFFBBBFRRR': (14, 7, 119),
            'BBFFBBFRLL': (102, 4, 820),
        }

    def test_decode_boarding_code(self):
        for k, v in self.boarding_codes.items():
            assert BinaryDecoder(k).decode() == v
