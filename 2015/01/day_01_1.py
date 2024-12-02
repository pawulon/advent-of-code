from pathlib import Path


def read_instructions(input_path: Path) -> str:
    return input_path.read_text()

def main():
    instructions = read_instructions(Path("input.txt"))
    floor = instructions.count("(") - instructions.count(")")
    print(floor)

if __name__ == '__main__':
    main()