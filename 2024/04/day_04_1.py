from pathlib import Path

XMAS = 'XMAS'
SAMX = 'SAMX'


def read_word_search(input_path: Path) -> list[str]:
    return input_path.read_text().splitlines()


def count_xmas(word_search: list[str]) -> int:
    count = 0
    for line in word_search:
        for i in range(len(line) - len(XMAS) + 1):
            current_word = line[i:i + len(XMAS)]
            if current_word in [XMAS, SAMX]:
                count += 1
    return count


def rotate_word_search(word_search: list[str]) -> list[str]:
    rotated_word_search = []
    max_x = len(word_search[0])
    max_y = len(word_search)
    for x in range(max_x):
        rotated_word_search.append("".join([word_search[y][x] for y in range(max_y)]))
    return rotated_word_search


def reverse_word_search(word_search: list[str]) -> list[str]:
    return [line[::-1] for line in word_search]


def get_word_search_diagonals(word_search: list[str]) -> list[str]:
    word_search_diagonals = []
    max_x = len(word_search[0])
    max_y = len(word_search)
    for y in range(max_y):
        word_search_diagonals.append("".join([word_search[y - x][x] for x in range(y + 1)]))
    for y in range(max_y - 1, 0, -1):
        word_search_diagonals.append("".join([word_search[max_y - 1 + y - x][x] for x in range(y, max_x)]))

    return word_search_diagonals


def main():
    word_search = read_word_search(Path("input.txt"))
    word_search_rotated = rotate_word_search(word_search)
    word_search_diagonals = get_word_search_diagonals(word_search)
    word_search_reversed = reverse_word_search(word_search)
    word_search_reversed_diagonals = get_word_search_diagonals(word_search_reversed)
    number_of_xmas = sum(
        map(count_xmas, [word_search, word_search_rotated, word_search_diagonals, word_search_reversed_diagonals]))
    print(number_of_xmas)


if __name__ == '__main__':
    main()
