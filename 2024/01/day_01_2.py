from collections import Counter
from pathlib import Path
from day_01_1 import read_lists




def main() -> None:
    left_list, right_list = read_lists(Path("input.txt"))
    right_list_locations_counter = Counter(right_list)
    similarity_score = sum([left_list[i] * right_list_locations_counter[left_list[i]]  for i in range(len(left_list))])
    print(similarity_score)


if __name__ == '__main__':
    main()
