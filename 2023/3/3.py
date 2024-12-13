import string
from pathlib import Path

puzzle = Path('puzzle').read_text()

schematic = puzzle.splitlines()

part_numbers = []

for y in range(len(schematic)):
    is_number_started = False
    is_number_a_part = False
    current_number = ''
    for x in range(len(schematic[y])):
        character = schematic[y][x]
        if character not in string.digits:
            if is_number_started:
                is_number_started = False
                if is_number_a_part:
                    part_numbers.append(int(current_number))
                    is_number_a_part = False
                current_number = ''
            continue

        if character in string.digits:
            current_number += character
            is_number_started = True

            if y - 1 >= 0:
                if x - 1 >= 0:
                    if schematic[y - 1][x - 1] not in ['.']:
                        is_number_a_part = True
                    if schematic[y - 1][x] not in ['.']:
                        is_number_a_part = True
                    if schematic[y][x - 1] not in string.digits + '.':
                        is_number_a_part = True

                if x + 1 < len(schematic[y]):
                    if schematic[y - 1][x - 1] not in ['.']:
                        is_number_a_part = True
                    if schematic[y - 1][x] not in string.digits + '.':
                        is_number_a_part = True
                    if schematic[y][x + 1] not in string.digits + '.':
                        is_number_a_part = True
            if y + 1 < len(schematic):
                if x - 1 >= 0:
                    if schematic[y + 1][x - 1] not in ['.']:
                        is_number_a_part = True
                    if schematic[y + 1][x] not in ['.']:
                        is_number_a_part = True
                    if schematic[y][x - 1] not in string.digits + '.':
                        is_number_a_part = True

                if x + 1 < len(schematic[y]):
                    if schematic[y + 1][x + 1] not in ['.']:
                        is_number_a_part = True


print(part_numbers)
print(sum(part_numbers))
