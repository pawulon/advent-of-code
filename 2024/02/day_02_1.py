from pathlib import Path


def read_levels(input_path: Path) -> list[list[int]]:
    with open(input_path, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def is_level_safe(level: list[int]) -> bool:
    direction = level[1] - level[0]
    for i in range(1, len(level)):
        difference = level[i] - level[i - 1]
        if not 0 < abs(difference) < 4 or direction * difference < 0:
            return False
    return True

def main() -> None:
    levels = read_levels(Path("input.txt"))
    number_of_safe_reports = sum([is_level_safe(level) for level in levels])
    print(number_of_safe_reports)

if __name__ == '__main__':
    main()
