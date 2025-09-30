import string

from typing import Any, Generator

PASSWORD: str = 'hxbxwxba'
FORBIDDEN_LETTERS: list[str] = ['i', 'o', 'l']
FORBIDDEN_INDEXES: list[int] = [string.ascii_letters.index(letter) for letter in FORBIDDEN_LETTERS]
NUMBER_OF_LETTERS: int = len(string.ascii_lowercase)


def find_next_valid_password(password: str) -> str:
    for new_password in find_next_password(password):
        if is_password_valid(new_password):
            return new_password
    return 'XXX'

def find_next_password(password: str) -> Generator[str, Any, None]:
    offsets = [string.ascii_lowercase.index(letter) for letter in password]
    while True:
        offsets[7] += 1
        for i in range(7, 0, -1):
            if offsets[i] == NUMBER_OF_LETTERS:
                offsets[i] = 0
                offsets[i - 1] += 1
        if any(x in FORBIDDEN_INDEXES for x in offsets):
            continue
        new_password = ''.join([string.ascii_lowercase[i] for i in offsets])
        yield new_password


def is_password_valid(password: str) -> bool:
    return (not does_contain_forbidden_letter(password) and
            does_contain_two_different_pairs(password) and
            does_contain_increasing_three_letters(password))


def does_contain_forbidden_letter(password: str) -> bool:
    if any([forbidden_letter in password for forbidden_letter in FORBIDDEN_LETTERS]):
        return True
    return False


def does_contain_two_different_pairs(password: str) -> bool:
    first_pair_letter: str = ''
    for i, letter in enumerate(password):
        if i == len(password) - 1:
            break
        if letter == password[i + 1]:
            if first_pair_letter == '':
                first_pair_letter = letter
            if letter != first_pair_letter:
                return True
    return False


def does_contain_increasing_three_letters(password: str) -> bool:
    for i, letter in enumerate(password):
        if i == len(password) - 2:
            break
        if ord(password[i + 2]) - ord(password[i + 1]) == ord(password[i + 1]) - ord(password[i]) == 1:
            return True
    return False


def main():
    print(find_next_valid_password('hxbxwxba'))


if __name__ == '__main__':
    main()
