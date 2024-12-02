from pathlib import Path
from typing import List
from day_02_1 import read_levels, is_level_safe


def is_level_safe_with_problem_dampener(level: List[int]) -> bool:
    is_increasing = level[1] - level[0]
    for i in range(1, len(level)):
        difference = level[i] - level[i - 1]
        if not 0 < abs(difference) < 4 or is_increasing * difference < 0:
            return (is_level_safe(level[0:i] + level[i + 1:]) or
                    is_level_safe(level[0:i - 1] + level[i:]) or
                    is_level_safe(level[0:i - 2] + level[i - 1:])
                    )
    return True


def main() -> None:
    levels = read_levels(Path("input.txt"))
    number_of_safe_reports = sum([is_level_safe_with_problem_dampener(level) for level in levels])
    print(number_of_safe_reports)


if __name__ == '__main__':
    main()
