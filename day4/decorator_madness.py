import re


def validate_byr(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\bbyr:(19[2-9]\d|200[012])\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_iyr(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\biyr:20(1\d|20)\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_eyr(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\beyr:20(2\d|30)\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_hgt(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\bhgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_hcl(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\bhcl:#[\da-f]{6}\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_ecl(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\becl:(amb|blu|brn|gry|grn|hzl|oth)\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper


def validate_pid(func):
    def wrapper(*args, **kwargs):
        if re.search(r"\bpid:\d{9}\b", func(*args, **kwargs)):
            return func(*args, **kwargs)
        return ""
    return wrapper

def count(func):
    def wrapper(*args, **kwargs):
        return int(bool(func(*args, **kwargs)))
    return wrapper

def total(func):
    def wrapper(*args, **kwargs):
        return sum(func(a, *args[1:], **kwargs) for a in args[0])
    return wrapper


def print_(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return wrapper


def read(func):
    def wrapper(*args, **kwargs):
        with open(args[0])as fh:
            return func*fh.read().split("\n\n")
    return wrapper

@print_
@total
@count
@validate_iyr
@validate_byr
@validate_eyr
@validate_hgt
@validate_hcl
@validate_ecl
@validate_pid
def solve(text):
    return text

with open("input.txt") as file_handle:
    text = file_handle.read().split("\n\n")
solve(text)
