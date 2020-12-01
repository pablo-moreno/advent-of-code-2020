def get_input_items(filename) -> list:
    with open(filename) as f:
        input_numbers = f.read().strip().splitlines()

    return [int(x) for x in input_numbers]


class DayOne(object):
    """
        Day 1, Report Repair

        TL; DR:
        - Given a integer list, find two numbers that sum 2020 and return the result of multiplying them.
        - Given a integer list, find three numbers that sum 2020 and return the result of multiplying them.

        https://adventofcode.com/2020/day/1
    """
    EXPECTED_RESULT = 2020

    def __init__(self, items: list):
        self.items: list = items

    @staticmethod
    def find_two_numbers_that_sum_2020(items: list) -> (int, int):
        """
            Returns the two numbers that sum 2020 from the input list
        """
        items.sort()

        for i in items:
            new_list = items.copy()
            new_list.remove(i)

            for j in new_list:
                if i + j == DayOne.EXPECTED_RESULT:
                    return i, j

            items.remove(i)

        return 1, -1

    @staticmethod
    def find_three_numbers_that_sum_2020(items: list) -> (int, int, int):
        """
            Returns three numbers that sum 2020 from an items list
        """
        items.sort()

        # Create a list of 2-length tuples that
        # its addition is less than 2020
        pairs = []
        for i in items:
            new_list = items.copy()
            new_list.remove(i)

            for j in new_list:
                if i + j <= DayOne.EXPECTED_RESULT:
                    pairs.append((i, j))
            items.remove(i)

        # Iterate over the pair list and look for a number
        # in the original list that added to the result gives 2020
        for pair in pairs:
            remainder = DayOne.EXPECTED_RESULT - sum(pair)

            if remainder in items:
                return remainder, *pair

        return 1, -1, 1

    def solve_first_part(self):
        items = self.items.copy()
        a, b = self.find_two_numbers_that_sum_2020(items)

        return a * b

    def solve_second_part(self):
        items = self.items.copy()
        a, b, c = self.find_three_numbers_that_sum_2020(items)

        return a * b * c


def main():
    lines = get_input_items('inputs/day_1.txt')
    result = DayOne(lines.copy()).solve_first_part()
    print(f'The result of the first puzzle is {result}')

    result = DayOne(lines.copy()).solve_second_part()
    print(f'The result of the second puzzle is {result}')


if __name__ == '__main__':
    main()
