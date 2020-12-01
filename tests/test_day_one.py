from unittest import TestCase
from ..day_one import DayOne


class DayOneTestCase(TestCase):
    def setUp(self):
        self.items = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]

    def test_sum_two_numbers_equal_2020(self):
        numbers = DayOne.find_two_numbers_that_sum_2020(self.items.copy())
        result = DayOne(self.items).solve_first_part()

        assert numbers == (299, 1721)
        assert sum(numbers) == 2020
        assert result == 514579

    def test_sum_three_numbers_equal_2020(self):
        numbers = DayOne.find_three_numbers_that_sum_2020(self.items.copy())
        result = DayOne(self.items).solve_second_part()

        assert numbers == (979, 675, 366)
        assert sum(numbers) == 2020
        assert result == 241861950
