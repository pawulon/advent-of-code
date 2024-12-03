from pathlib import Path

from day_02_1 import read_presents, Present


def calculate_ribbon_requirement(present: Present) -> int:
    side_requirement = calculate_side_requirement(present)
    bow_requirement = calculate_cubic_volume(present)
    return side_requirement + bow_requirement


def calculate_side_requirement(present: Present) -> int:
    a, b = find_two_smallest_dimensions(present)
    return calculate_perimeter(a, b)


def calculate_cubic_volume(present: Present) -> int:
    l, w, h = present
    return l * w * h


def find_two_smallest_dimensions(present: Present) -> tuple[int, int]:
    l, w, h = present
    sorted_dimensions = sorted([l, w, h])
    return sorted_dimensions[0], sorted_dimensions[1]


def calculate_perimeter(a: int, b: int) -> int:
    return 2 * a + 2 * b


def main():
    presents = read_presents(Path("input.txt"))
    total_ribbon_requirement = sum([calculate_ribbon_requirement(present) for present in presents])
    print(total_ribbon_requirement)


if __name__ == '__main__':
    main()
