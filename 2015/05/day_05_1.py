from pathlib import Path


def read_strings(input_path: Path) -> list[str]:
    return input_path.read_text().split()


def is_nice_string(string: str) -> bool:
    if does_contain_forbidden_strings(string):
        return False
    if not does_contain_at_least_one_letter_that_appears_twice_in_a_row(string):
        return False
    if not does_contain_at_least_three_vowels(string):
        return False

    return True


def does_contain_forbidden_strings(string: str) -> bool:
    return any(element in string for element in ["ab", "cd", "pq", "xy"])


def does_contain_at_least_three_vowels(string: str) -> bool:
    number_of_vowels_in_string = sum([string.count(vowel) for vowel in "aeiou"])
    if number_of_vowels_in_string >= 3:
        return True
    return False


def does_contain_at_least_one_letter_that_appears_twice_in_a_row(string: str) -> bool:
    previous_character = ''
    for character in string:
        if character == previous_character:
            return True
        previous_character = character
    return False


def main():
    strings = read_strings(Path("input.txt"))
    number_of_nice_strings = sum([is_nice_string(string) for string in strings])
    print(number_of_nice_strings)


if __name__ == '__main__':
    main()
