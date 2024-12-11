from functools import lru_cache
from pathlib import Path


def read_stones(input_path: Path) -> list[int]:
    return list(map(int, input_path.read_text().split()))


def blink(stones: list[int]) -> list[int]:
    new_list = []
    for stone in stones:
        new_list += apply_rule(stone)
    return new_list


@lru_cache
def apply_rule(stone: int) -> list[int]:
    if not stone:
        return [1]
    elif not len(str(stone)) % 2:
        length = len(str(stone))
        middle = length // 2
        return [(int(str(stone)[:middle])), (int(str(stone)[middle:]))]
    else:
        return [stone * 2024]


def main():
    stones = read_stones(Path("input.txt"))
    for _ in range(25):
        stones = blink(stones)
        print(len(stones))


if __name__ == '__main__':
    main()
