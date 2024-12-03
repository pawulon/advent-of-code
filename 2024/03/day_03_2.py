from pathlib import Path
from day_03_1 import read_memory, get_multiplications, calculate_result


def clear_excluded_multiplications(memory: str) -> str:
    dont = "don't()"
    do = "do()"
    dont_length = len(dont)
    do_length = len(do)
    enabled = True
    cleared_memory = ""
    for i in range(len(memory) - dont_length):
        if memory[i:i + dont_length] == "don't()":
            enabled = False
            i += dont_length
            continue
        if memory[i:i + do_length] == "do()":
            enabled = True
            i += do_length
            continue
        if enabled:
            cleared_memory += memory[i]
    cleared_memory += memory[-dont_length:]
    return cleared_memory


def main() -> None:
    memory = read_memory(Path("input.txt"))
    memory = clear_excluded_multiplications(memory)
    multiplications = get_multiplications(memory)
    result = calculate_result(multiplications)
    print(result)


if __name__ == '__main__':
    main()
