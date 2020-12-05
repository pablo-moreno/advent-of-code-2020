def get_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


class BinaryDecoder(object):
    def __init__(self, code):
        self.code = code

    def get_binary_sum(self, series, control_character):
        """
            Returns the binary sum of a given series with a control_character that represents the truthy value.
        """
        return sum([2 ** i if char == control_character else 0 for i, char in enumerate(series[::-1])])

    def decode(self) -> (int, int, int):
        row_characters = self.code[:7]
        column_characters = self.code[7:]
        row_code = self.get_binary_sum(row_characters, control_character='B')
        column_code = self.get_binary_sum(column_characters, control_character='R')

        return row_code, column_code, row_code * 8 + column_code


class DayFive(object):
    """
        Day 5, Binary Boarding
        https://adventofcode.com/2020/day/5

        TL; DR:
        - Find the greatest Seat ID given a list of boarding codes, represented by binary codes
          with F=0, B=1 for rows and R=1, L=0 for columns.

        - Find the missing Seat ID in the list, checking that Seat ID +1 and -1 are present.
    """

    @staticmethod
    def solve_first_part(input_data):
        seat_ids = []
        for line in input_data:
            row_code, column_code, seat_id = BinaryDecoder(line).decode()
            seat_ids.append(seat_id)

        return max(seat_ids)

    @staticmethod
    def solve_second_part(input_data):
        seat_ids = []
        for line in input_data:
            row_code, column_code, seat_id = BinaryDecoder(line).decode()
            seat_ids.append(seat_id)

        seat_ids.sort()
        min_id, *rest, max_id = seat_ids
        diff = set(range(min_id, max_id + 1)).difference(set(seat_ids))

        for item in diff:
            if item + 1 in seat_ids and item - 1 in seat_ids:
                return item
        else:
            return None


if __name__ == '__main__':
    data = get_input('inputs/day_05.txt')

    result = DayFive.solve_first_part(data)
    print(f'The result of the first part is {result}')

    result = DayFive.solve_second_part(data)
    print(f'The result of the second part is {result}')
