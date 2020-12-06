def get_input(filename):
    with open(filename) as f:
        return f.read().split('\n\n')


class DaySix(object):
    """
        Day 6, Custom Customs
        https://adventofcode.com/2020/day/6

        TL; DR:
        - Count all the different responses given from a group
        - Sum all the affirmative answers common to a group
    """
    @staticmethod
    def parse_input(data):
        answer_groups = []

        for group in data:
            answer_groups.append(group.split('\n'))

        return answer_groups

    @staticmethod
    def solve_first_part(data):
        total = 0
        for group in data:
            answer_set = set()

            for answer in group:
                for letter in answer:
                    answer_set.add(letter)

            total += len(answer_set)

        return total

    @staticmethod
    def solve_second_part(data):
        total = 0

        for group in data:
            answer_set = set()

            for i, answers in enumerate(group):
                if i == 0:
                    answer_set = set(answers)
                else:
                    answer_set = answer_set.intersection(set(answers))

            group_length = len(answer_set)
            total += group_length

        return total


if __name__ == '__main__':
    input_data = get_input('inputs/day_06.txt')
    parsed = DaySix.parse_input(input_data)

    result = DaySix.solve_first_part(parsed)
    print(f'The result of the first part is {result}')

    result = DaySix.solve_second_part(parsed)
    print(f'The result of the second part is {result}')
