from pathlib import Path

from day_01_1 import read_instructions


def which_character_will_cause_santa_enter_basement(instructions: str) -> int:
    floor = 0
    for i, character in enumerate(instructions):
        match character:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor < 0:
            return i + 1


def main():
    instructions = read_instructions(Path("input.txt"))
    character_index = which_character_will_cause_santa_enter_basement(instructions)
    print(character_index)


if __name__ == '__main__':
    main()
