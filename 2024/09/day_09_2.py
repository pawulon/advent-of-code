from dataclasses import dataclass
from pathlib import Path
from day_09_1 import read_disk_map, get_individual_representation, calculate_checksum


@dataclass
class Block:
    file_index: str
    length: int
    list_index: int


def move_file_blocks(individual_representation: list[str]) -> list[str]:
    blocks = get_blocks(individual_representation)
    for block in blocks:
        fit_block(individual_representation, block)
    return individual_representation


def fit_block(representation: list[str], block: Block) -> None:
    current_block = ""
    for i in range(block.list_index):
        if representation[i] == current_block:
            continue
        else:
            current_block = representation[i]
        if representation[i] == ".":
            required_length = get_length_of_block(representation, i)
            if block.length <= required_length:
                for j in range(block.length):
                    representation[i + j] = block.file_index
                for j in range(block.list_index, block.list_index + block.length):
                    representation[j] = "."
                break


def get_blocks(individual_representation: list[str]) -> list[Block]:
    repr_copy = individual_representation[::]
    skip = 0
    blocks = []
    for i in range(len(repr_copy)):
        if repr_copy[i] == ".":
            continue
        if skip:
            skip -= 1
            continue

        length = get_length_of_block(repr_copy, i)
        skip = length - 1
        blocks.append(Block(file_index=repr_copy[i], length=length, list_index=i))
    return blocks[::-1]


def get_length_of_block(individual_representation: list[str], index: int) -> int:
    element = individual_representation[index]
    length = 0
    for i in range(index, len(individual_representation)):
        if individual_representation[i] == element:
            length += 1
        else:
            break
    return length


def main():
    disk_map = read_disk_map(Path("input.txt"))
    individual_representation = get_individual_representation(disk_map)
    reordered_files = move_file_blocks(individual_representation)
    checksum = calculate_checksum(reordered_files)
    print(checksum)


if __name__ == '__main__':
    main()
