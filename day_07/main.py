from collections import defaultdict
from functools import reduce


def get_input(filename):
    with open(filename) as f:
        return f.readlines()


def parse_bag(bag):
    parent_bag, bags = bag.strip().split(' bags contain ')

    content = defaultdict(int)
    for comp in bags.split(', '):
        words = comp.split(' ')

        if words[0] != 'no':
            content[words[1] + ' ' + words[2]] = int(words[0])

    return parent_bag, content


def recursive_parents(bags, bag_name):
    parents = set(parent_name for parent_name, parent_contents in bags.items() if bag_name in parent_contents)
    return reduce(lambda a, b: a.union(recursive_parents(bags, b)), parents, parents)


def num_recursive_children(bags, bag):
    return reduce(lambda a, t: a + t[1] * (1 + num_recursive_children(bags, bags[t[0]])), bag.items(), 0)


class DaySeven(object):
    @staticmethod
    def solve_first_part(input_data):
        bags = dict(parse_bag(l) for l in input_data)
        return len(recursive_parents(bags, 'shiny gold'))

    @staticmethod
    def solve_second_part(input_data):
        bags = dict(parse_bag(l) for l in input_data)
        return num_recursive_children(bags, bags['shiny gold'])


if __name__ == '__main__':
    lines = get_input('inputs/day_07.txt')
    result = DaySeven.solve_first_part(lines)
    print(f'The result of the first part is {result}')

    result = DaySeven.solve_second_part(lines)
    print(f'The result of the second part is {result}')

