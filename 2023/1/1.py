import re
from pathlib import Path
from typing import Tuple

puzzle = Path('puzzle').read_text()

DIGIT_REGEX = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

DIGITS = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9'}


def translate_digit(digit: str) -> str:
    if digit in DIGITS.keys():
        return DIGITS[digit]
    return digit


def find_first_and_last_digit(text: str) -> Tuple[str, str]:
    digits = re.findall(DIGIT_REGEX, text)
    return digits[0], digits[-1]


def get_calibration_value(text: str) -> int:
    first_digit, last_digit = find_first_and_last_digit(text)
    return int(translate_digit(first_digit) + translate_digit(last_digit))

#
# for line in puzzle.splitlines():
#     calibration_value = get_calibration_value(line)
#     print(calibration_value, line)

sum_of_calibration_values = sum([get_calibration_value(line) for line in puzzle.splitlines()])
print(sum_of_calibration_values)
