from pathlib import Path

import re


def read_memory(input_path: Path) -> str:
    return input_path.read_text()


def get_multiplications(memory: str) -> list[tuple[str, str]]:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, memory)
    return matches


def calculate_result(multiplications: list[tuple[str, str]]) -> int:
    return sum([int(numbers[0]) * int(numbers[1]) for numbers in multiplications])


def main() -> None:
    memory = read_memory(Path("input.txt"))
    multiplications = get_multiplications(memory)
    result = calculate_result(multiplications)
    print(result)


if __name__ == '__main__':
    main()
