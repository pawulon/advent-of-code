from pathlib import Path
from typing import List


def read_levels(input_path: Path) -> List[List[int]]:
    with open(input_path, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def is_level_safe(level: List[int]) -> bool:
    is_increasing = level[1] - level[0]
    for i in range(1, len(level)):
        difference = level[i] - level[i - 1]
        if not 0 < abs(difference) < 4 or is_increasing * difference < 0:
            return False
    return True

def main() -> None:
    levels = read_levels(Path("input.txt"))
    number_of_safe_reports = sum([is_level_safe(level) for level in levels])
    print(number_of_safe_reports)

if __name__ == '__main__':
    main()
