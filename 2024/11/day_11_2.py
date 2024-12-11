from functools import lru_cache
from pathlib import Path
from day_11_1 import read_stones, apply_rule


@lru_cache(maxsize=None)
def count_stones_after_blinks(stones: tuple[int, ...], number_of_blinks: int) -> int:
    number_of_stones = 0
    if number_of_blinks == 0:
        return len(stones)
    for stone in stones:
        number_of_stones += count_stones_after_blinks(apply_rule(stone), number_of_blinks - 1)
    return number_of_stones


def main():
    stones = read_stones(Path("input.txt"))
    stone_count = count_stones_after_blinks(stones, 75)
    print(stone_count)


if __name__ == '__main__':
    main()
