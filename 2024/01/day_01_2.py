from pathlib import Path
from day_01_1 import read_lists


def main() -> None:
    left_list, right_list = read_lists(Path("input.txt"))
    similarity_score = sum([index * right_list.count(index) for index in left_list])
    print(similarity_score)


if __name__ == '__main__':
    main()
