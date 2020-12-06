from unittest import TestCase
from . import DaySix

RAW_DATA =\
"""abc

a
b
c

ab
ac

a
a
a
a

b"""


class DaySixTestCase(TestCase):
    def test_parse_data(self):
        parsed = DaySix.parse_input(RAW_DATA.split('\n\n'))
        assert parsed == [
            ['abc'],
            ['a', 'b', 'c'],
            ['ab', 'ac'],
            ['a', 'a', 'a', 'a'],
            ['b']
        ]

    def test_first_part(self):
        parsed = DaySix.parse_input(RAW_DATA.split('\n\n'))
        result = DaySix.solve_first_part(parsed)
        assert result == 11

    def test_second_part(self):
        parsed = DaySix.parse_input(RAW_DATA.split('\n\n'))
        result = DaySix.solve_second_part(parsed)
        assert result == 6
