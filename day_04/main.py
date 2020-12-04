import re
from dataclasses import dataclass
from typing import List, Tuple, Type


def get_input(filename):
    with open(filename) as f:
        return f.read()


@dataclass
class Passport(object):
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None


class ValidationCriteria(object):
    def __init__(self, instance):
        self.instance = instance

    def is_valid(self) -> bool:
        raise NotImplementedError("You must implement .is_valid() function")


class ValidationCriteriaMixin(object):
    criteria_classes: Tuple[Type[ValidationCriteria]] = ()

    def is_valid(self) -> bool:
        for criteria in self.criteria_classes:
            is_valid = criteria(self).is_valid()

            if not is_valid:
                print(criteria.__name__, self)
                return False

        return True


class PassportValidation(Passport, ValidationCriteriaMixin):
    pass


class AllFieldsCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        return all([
            self.instance.byr,
            self.instance.iyr,
            self.instance.eyr,
            self.instance.hgt,
            self.instance.hcl,
            self.instance.ecl,
            self.instance.pid,
        ])


class BirthYearCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        try:
            return int(self.instance.byr) in range(1920, 2003)
        except Exception as e:
            return False


class IssueYearCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        try:
            return int(self.instance.iyr) in range(2010, 2021)
        except Exception as e:
            return False


class ExpirationYearCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        try:
            return int(self.instance.eyr) in range(2020, 2031)
        except Exception as e:
            return False


class HeightCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        try:
            if 'cm' in self.instance.hgt:
                value, rest = self.instance.hgt.split('cm')
                return int(value) in range(150, 194)
            elif 'in' in self.instance.hgt:
                value, rest = self.instance.hgt.split('in')
                return int(value) in range(59, 76)
            else:
                return False
        except Exception as e:
            print(str(e))
            return False


class HairColorCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        return bool(re.match(r'#[a-f0-9]{6}', self.instance.hcl))


class EyeColorCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        return self.instance.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth", ]


class PassportIdCriteria(ValidationCriteria):
    def is_valid(self) -> bool:
        return bool(re.match(r'[0-9]{9}', self.instance.pid))


class FirstPartPassportValidation(PassportValidation):
    criteria_classes = (AllFieldsCriteria, )


class SecondPartPassportValidation(PassportValidation):
    criteria_classes = (
        AllFieldsCriteria,
        BirthYearCriteria,
        IssueYearCriteria,
        ExpirationYearCriteria,
        HeightCriteria,
        HairColorCriteria,
        EyeColorCriteria,
        PassportIdCriteria,
    )


class DayFour(object):
    @staticmethod
    def parse_data(input_data: str, part=1) -> List[PassportValidation]:
        passports_raw_data = input_data.split('\n\n')

        passports = []

        for item in passports_raw_data:
            passport_raw_data = ' '.join(item.lstrip().rstrip().split('\n')).split(' ')
            passport_data = []

            for kv in passport_raw_data:
                try:
                    k, v = kv.split(':')
                    passport_data.append((k, v))
                except ValueError as e:
                    print(f'Error parsing {kv}: {str(e)}')

            if part == 1:
                passports.append(FirstPartPassportValidation(**dict(passport_data)))
            else:
                passports.append(SecondPartPassportValidation(**dict(passport_data)))

        return passports

    @staticmethod
    def solve(passports: List[PassportValidation]):
        valid = 0
        invalid_passports = []

        for passport in passports:
            if passport.is_valid():
                valid += 1
            else:
                invalid_passports.append(passport)

        return valid


if __name__ == '__main__':
    data = get_input('inputs/day_04.txt')
    part_one_passports = DayFour.parse_data(data, part=1)
    result = DayFour.solve(part_one_passports)
    print(f'The result of the first part is {result}.')

    part_two_passports = DayFour.parse_data(data, part=2)
    result = DayFour.solve(part_two_passports)
    print(f'The result of the second part is {result}')
