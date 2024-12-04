from pathlib import Path
from day_04_1 import read_word_search


def count_x_mas(word_search: list[str]) -> int:
    max_y = len(word_search)
    x_mas_count = 0
    for y in range(1, max_y - 1):
        for x in range(1, max_y - 1):
            square_3_by_3 = get_square_3_by_3(word_search, x, y)
            if is_this_x_mas(square_3_by_3):
                x_mas_count += 1
    return x_mas_count


def get_square_3_by_3(word_search: list[str], x: int, y: int) -> list[str]:
    return [word_search[y][x - 1] + word_search[y][x] + word_search[y][x + 1] for y in range(y - 1, y + 2)]


def is_this_x_mas(fields: list[str]) -> bool:
    left_diagonal = fields[0][0] + fields[1][1] + fields[2][2]
    right_diagonal = fields[0][2] + fields[1][1] + fields[2][0]
    if left_diagonal in ['MAS', 'SAM'] and right_diagonal in ['MAS', 'SAM']:
        return True
    return False


def main():
    word_search = read_word_search(Path("input.txt"))
    print(count_x_mas(word_search))


if __name__ == '__main__':
    main()
