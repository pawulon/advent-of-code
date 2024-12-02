from pathlib import Path
from day_05_1 import read_strings


def is_nice_string(string: str) -> bool:
    if not does_contain_a_pair_of_two_chars_appearing_more_than_once(string):
        return False
    if not does_contain_a_letter_which_repeats_with_one_letter_between(string):
        return False
    return True


def does_contain_a_letter_which_repeats_with_one_letter_between(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


def does_contain_a_pair_of_two_chars_appearing_more_than_once(string: str) -> bool:
    for i in range(len(string) - 1):
        if string[i] + string[i+1] in string[i+2:]:
            return True
    return False


def main():
    strings = read_strings(Path("input.txt"))
    number_of_nice_strings = sum([is_nice_string(string) for string in strings])
    print(number_of_nice_strings)


if __name__ == '__main__':
    main()