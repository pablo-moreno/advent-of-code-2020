from math import ceil
from typing import List


def get_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


class DayThree(object):
    """
        Day 3, Toboggan Trajectory

        TL; DR:

        - Given a pattern, move in a x=-3, y=-1 trajectory and check if you find a tree (#)
          and return the number of trees that you have encountered.

        - Given a pattern and trajectory directions, move and check if you find a tree (#)
          and return the result of multiplying the number of trees that you have encountered.

        https://adventofcode.com/2020/day/3
    """

    @staticmethod
    def get_complete_pattern(data: List[str], x: int, y: int) -> (List[str], int):
        total_y = len(data)
        repeats = ceil(total_y * x / len(data[0]))
        pattern = [line * repeats for line in data]

        return pattern

    @staticmethod
    def get_encountered_trees(pattern: List[str], x_move: int, y_move: int):
        current_position = (0, 0)
        trees_count = 0

        for i, line in enumerate(pattern[::y_move]):
            x, y = current_position

            if line[x] == '#':
                trees_count += 1

            current_position = (x + x_move, y + y_move)

        return trees_count

    @staticmethod
    def solve_first_part(pattern):
        x, y = (3, 1)
        pattern = DayThree.get_complete_pattern(pattern, x, y)

        return DayThree.get_encountered_trees(pattern, x, y)

    @staticmethod
    def solve_second_part(pattern):
        result = 1
        trees_found = []
        movements = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]

        for x, y in movements:
            pattern = DayThree.get_complete_pattern(pattern, x, y)
            encountered_trees = DayThree.get_encountered_trees(pattern, x, y)
            trees_found.append(encountered_trees)
            result *= encountered_trees

        return result


def main():
    data = get_input('inputs/day_03.txt')
    result = DayThree.solve_first_part(data)
    print(f'The result of the first part is {result}')

    result = DayThree.solve_second_part(data)
    print(f'The result of the second part is {result}')


if __name__ == "__main__":
    main()
