from unittest import TestCase
from . import DayThree


class DayThreeTestCase(TestCase):
    def setUp(self):
        self.data = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
        ]

    def test_first_part(self):
        x_move, y_move = 3, 1
        pattern = DayThree.get_complete_pattern(self.data, x=x_move, y=y_move)
        result = DayThree.solve_first_part(pattern)
        assert result == 7

    def test_second_part(self):
        result = DayThree.solve_second_part(self.data)
        assert result == 336
