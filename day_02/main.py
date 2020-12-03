def get_input(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


class DayTwo(object):
    """
        Day 1, Password Philosophy

        TL; DR:
        - Given a password list, check if it contains the specified range of the specified letter.
        - Given a password list, check if the specified letter is placed at one of the positions given.

        https://adventofcode.com/2020/day/2
    """
    @staticmethod
    def parse_line(line: str) -> (str, str, str):
        constraint_str, password = line.split(':')
        letter_range, letter = constraint_str.split(' ')

        return letter, letter_range, password.strip()

    @staticmethod
    def validate_password_first_part(letter: str, letter_range: str, password: str) -> bool:
        min_chars, max_chars = [int(x) for x in letter_range.split('-')]
        count = 0

        for char in password:
            if char == letter:
                count += 1

        return min_chars <= count <= max_chars

    @staticmethod
    def validate_password_second_part(letter: str, letter_range: str, password: str) -> bool:
        valid_positions = {int(x) for x in letter_range.split('-')}
        positions = set()

        for i, char in enumerate(password, start=1):
            if char == letter:
                positions.add(i)

        return len(positions.intersection(valid_positions)) == 1

    @staticmethod
    def solve_first_part(lines):
        valid_passwords = 0

        for line in lines:
            letter, letter_range, password = DayTwo.parse_line(line)

            if DayTwo.validate_password_first_part(letter, letter_range, password):
                valid_passwords += 1

        return valid_passwords

    @staticmethod
    def solve_second_part(lines):
        valid_passwords = 0

        for line in lines:
            letter, letter_range, password = DayTwo.parse_line(line)

            if DayTwo.validate_password_second_part(letter, letter_range, password):
                valid_passwords += 1

        return valid_passwords


def main():
    lines = get_input('inputs/day_02.txt')
    result = DayTwo.solve_first_part(lines)
    print(f'The result of the first puzzle is {result}')

    result = DayTwo.solve_second_part(lines)
    print(f'The result of the second puzzle is {result}')


if __name__ == '__main__':
    main()
