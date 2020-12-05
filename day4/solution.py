import argparse
import re


class PassportParser:

    @classmethod
    def load_passport_from_data(cls, data):
        passport_fields = cls.extract_fields_from_data(data)
        return Passport(**passport_fields)

    @classmethod
    def extract_fields_from_data(cls, data):
        return {
            "id": cls._extract_field("pid", data),
            "birth_year" : cls._extract_field("byr", data),
            "issue_year" : cls._extract_field("iyr", data),
            "expiration_year" : cls._extract_field("eyr", data),
            "height" : cls._extract_field("hgt", data),
            "hair_colour" : cls._extract_field("hcl", data),
            "eye_colour" : cls._extract_field("ecl", data),
            "country_id" : cls._extract_field("cid", data),
        }

    @classmethod
    def _extract_field(cls, field_name, data):
        values_found = re.findall(rf"(?<=\b{field_name}:)[#\w\d]+", data)
        if len(values_found) != 1:
            # Error should either be logged or thrown here - unclear but I'm not going to care for this
            return ""
        return values_found.pop()


class Passport:

    validate_fields = False

    max_valid_birth_year = 2002
    min_valid_birth_year = 1920
    max_valid_issue_year = 2020
    min_valid_issue_year = 2010
    max_valid_expiration_year = 2030
    min_valid_expiration_year = 2020
    valid_eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    max_valid_height_cm = 193
    min_valid_height_cm = 150
    max_valid_height_in = 76
    min_valid_height_in = 59

    @classmethod
    def turn_on_field_validation(cls):
        cls.validate_fields = True

    def __init__(self, id, birth_year, issue_year, expiration_year, height, hair_colour, eye_colour, country_id):
        self._id = id
        self._birth_year = birth_year
        self._issue_year = issue_year
        self._expiration_year = expiration_year
        self._height = height
        self._hair_colour = hair_colour
        self._eye_colour = eye_colour
        self._country_id = country_id

    def __repr__(self):
        return (
            "<Passport("
            f"id={self._id}, "
            f"birth_year={self._birth_year}, "
            f"issue_year={self._issue_year}, "
            f"expiration_year={self._expiration_year}, "
            f"height={self._height}, "
            f"hair_colour={self._hair_colour}, "
            f"eye_colour={self._eye_colour}, "
            f"country_id={self._country_id}, "
            ")>"
        )

    def is_valid(self):
        if self.validate_fields:
            return self.check_fields_exist() and self.check_fields_are_valid()
        else:
            return self.check_fields_exist()

    def check_fields_exist(self):
        return bool(
            self._id
            and self._birth_year
            and self._issue_year
            and self._expiration_year
            and self._height
            and self._hair_colour
            and self._eye_colour
        )

    def check_fields_are_valid(self):
        return (
            self.has_valid_id
            and self.has_valid_birth_year
            and self.has_valid_issue_year
            and self.has_valid_expiration_year
            and self.has_valid_height
            and self.has_valid_hair_colour
            and self.has_valid_eye_colour
        )

    @property
    def has_valid_id(self):
        return bool(re.match(r"\d{9}$", self._id))

    @property
    def has_valid_birth_year(self):
        return self._validate_year(self._birth_year, self.max_valid_birth_year, self.min_valid_birth_year)

    @property
    def has_valid_issue_year(self):
        return self._validate_year(self._issue_year, self.max_valid_issue_year, self.min_valid_issue_year)

    @property
    def has_valid_expiration_year(self):
        return self._validate_year(self._expiration_year, self.max_valid_expiration_year, self.min_valid_expiration_year)

    @property
    def has_valid_height(self):
        height_pattern_match = re.match(r"(\d+)(cm|in)$", self._height)
        try:
            value, unit = height_pattern_match.group(1), height_pattern_match.group(2)
            value = int(value)
        except (AttributeError, ValueError):
            return False
        else:
            return self._validate_height(value, unit)

    @property
    def has_valid_hair_colour(self):
        return bool(re.match(r"#[\da-f]{6}$", self._hair_colour))

    @property
    def has_valid_eye_colour(self):
        return self._eye_colour in self.valid_eye_colours

    def _validate_height(self, value, unit):
        if unit == "cm":
            return self._validate_height_cm(value)
        elif unit == "in":
            return self._validate_height_in(value)
        else:
            return False

    def _validate_height_cm(self, value):
        return self.min_valid_height_cm <= value <= self.max_valid_height_cm

    def _validate_height_in(self, value):
        return self.min_valid_height_in <= value <= self.max_valid_height_in

    def _validate_year(self, year, max_year, min_year):
        try:
            year = int(year)
        except ValueError:
            return False
        else:
            return min_year <= year <= max_year


class Passports:

    passport_delimiter = "\n\n"

    def parse_data_from_file(self, file):
        with open(file) as file_handle:
            data = file_handle.read()
        self._passports = [PassportParser.load_passport_from_data(datum) for datum in data.split(self.passport_delimiter)]

    def count_valid_passports(self):
        return len([passport for passport in self._passports if passport.is_valid()])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Advent of Code Day 4")

    parser.add_argument("input_file", help="The file to be parsed and validated")
    parser.add_argument("--part", choices=[1,2], default=1, type=int, help="The part of the problem that is being run")

    args = parser.parse_args()
    if args.part == 2:
        Passport.turn_on_field_validation()

    passports = Passports()
    passports.parse_data_from_file(args.input_file)

    numbers_of_valid_passports = passports.count_valid_passports()
    print(f"There are {numbers_of_valid_passports} valid passports in {args.input_file}")
