from pathlib import Path
from typing import Tuple, List


def read_lists(input_path: Path) -> Tuple[List[int], List[int]]:
    left_list = []
    right_list = []
    with open(input_path, 'r') as file:
        for line in file:
            a, b = line.split()
            left_list.append(int(a))
            right_list.append(int(b))
    return left_list, right_list


def main() -> None:
    left_list, right_list = read_lists(Path("input.txt"))
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    total_distance = sum([abs(left_list[i] - right_list[i]) for i in range(len(left_list))])
    print(total_distance)


if __name__ == '__main__':
    main()
