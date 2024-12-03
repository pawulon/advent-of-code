from pathlib import Path

Present = tuple[int, int, int]

def read_presents(input_path: Path) -> list[Present]:
    presents = []
    with open(input_path, 'r') as file:
        for line in file:
            l, w, h = line.split("x")
            presents.append((int(l), int(w), int(h)))
    return presents

def calculate_paper_requirement(present: Present) -> int:
    l, w, h = present
    return 2 * l * w + 2 * h * w + 2 * h * l + min(l * w, w * h, h * l)

def main():
    presents = read_presents(Path("input.txt"))
    total_paper_needed = sum([calculate_paper_requirement(present) for present in presents])
    print(total_paper_needed)

if __name__ == '__main__':
    main()
