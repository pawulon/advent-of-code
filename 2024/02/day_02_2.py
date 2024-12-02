from pathlib import Path
from typing import List
from day_02_1 import read_levels, is_level_safe


def is_level_safe_with_problem_dampener(level: List[int]) -> bool:
    is_increasing = level[1] - level[0]
    for i in range(1, len(level)):
        difference = level[i] - level[i - 1]
        if not 0 < abs(difference) < 4 or is_increasing * difference < 0:
            return (is_level_safe(list_without_element_at_index(level, i)) or
                    is_level_safe(list_without_element_at_index(level, i-1)) or
                    is_level_safe(list_without_element_at_index(level, i-2))
                    )
    return True

def list_without_element_at_index(lst: List[int], index: int) -> List[int]:
    return lst[:index] + lst[index + 1:]

def main() -> None:
    levels = read_levels(Path("input.txt"))
    number_of_safe_reports = sum([is_level_safe_with_problem_dampener(level) for level in levels])
    print(number_of_safe_reports)


if __name__ == '__main__':
    main()
