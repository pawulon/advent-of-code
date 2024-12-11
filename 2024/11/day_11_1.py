from pathlib import Path


def read_stones(input_path: Path) -> tuple[int, ...]:
    return tuple(map(int, input_path.read_text().split()))


def blink(stones: tuple[int, ...]) -> tuple[int, ...]:
    new_list = []
    for stone in stones:
        new_list += apply_rule(stone)
    return new_list


def apply_rule(stone: int) -> tuple[int, ...]:
    if not stone:
        return (1,)
    stone_string = str(stone)
    length = len(stone_string)
    if not length % 2:
        middle = length // 2
        return (int(stone_string[:middle])), (int(stone_string[middle:]))
    return (stone * 2024,)


def main():
    stones = read_stones(Path("input.txt"))
    for _ in range(25):
        stones = blink(stones)
    print(len(stones))


if __name__ == '__main__':
    main()
