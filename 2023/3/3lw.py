# day03_1.py

import re


def get_numbers_and_symbols(filename: str) -> tuple:
    with open(filename, mode='r') as f:
        numbers = []
        symbols = {}
        for line_no, line in enumerate(f):
            result = re.finditer(r'(\d+)', line.strip())
            for match in result:
                numbers.append({'number': int(match.group()), 'row': line_no, 'span': match.span()})

            result = re.finditer(r'([^\d.])', line.strip())
            for match in result:
                symbols[(line_no, match.start())] = match.group()
        return numbers, symbols


def find_engine_parts(schematics_numbers, schematics_symbols):
    sum_of_parts = 0
    list_of_parts = []
    for number in schematics_numbers:
        if is_number_adjacent_to_symbol(number['row'], number['span'], schematics_symbols):
            sum_of_parts += number['number']
            list_of_parts.append(number['number'])
    print(list_of_parts)
    return sum_of_parts


def is_number_adjacent_to_symbol(x_pos, span, symbol_dict: dict):
    is_adjacent: bool = False
    for position in get_positions_to_check(x_pos, span):
        if position in symbol_dict.keys():
            is_adjacent = True
            break
    return is_adjacent


def get_positions_to_check(x_pos, span):
    positions_to_check = []
    for row in range(x_pos - 1, x_pos + 2):
        for column in range(span[0] - 1, span[1] + 1):
            positions_to_check.append((row, column))
    return positions_to_check


if __name__ == "__main__":
    numbers, symbols = get_numbers_and_symbols('puzzle')
    print(find_engine_parts(numbers, symbols))