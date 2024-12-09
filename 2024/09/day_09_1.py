from pathlib import Path


def read_disk_map(input_path: Path) -> str:
    return input_path.read_text()


def get_individual_representation(disk_map: str) -> list[str]:
    individual_representation = []
    index = 0
    is_this_file_block = True
    for digit in disk_map:
        for _ in range(int(digit)):
            if is_this_file_block:
                individual_representation.append(str(index))
            else:
                individual_representation.append(".")
        if is_this_file_block:
            index += 1
        is_this_file_block = not is_this_file_block
    return individual_representation


def move_file_blocks(individual_representation: list[str]) -> list[str]:
    clean_copy = [element for element in individual_representation if element != "."]
    gap_fixed = 0
    i = 0
    for i, element in enumerate(individual_representation):
        if element == '.':
            individual_representation[i] = clean_copy.pop()
            gap_fixed += 1
        if len(clean_copy) + gap_fixed == i:
            break
    return individual_representation[:i]


def calculate_checksum(files: list[str]) -> int:
    return sum([i * int(file_index) for i, file_index in enumerate(files) if file_index != "."])


def main():
    disk_map = read_disk_map(Path("input.txt"))
    individual_representation = get_individual_representation(disk_map)
    reordered_files = move_file_blocks(individual_representation)
    checksum = calculate_checksum(reordered_files)
    print(checksum)


if __name__ == '__main__':
    main()
