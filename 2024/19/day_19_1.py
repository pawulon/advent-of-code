from pathlib import Path


def read_towels_and_designs(input_path: Path) -> tuple[list[str], list[str]]:
    lines = input_path.read_text().splitlines()
    towels = [towel.strip() for towel in lines[0].split(",")]
    designs = [line for line in lines[2:]]
    return towels, designs


def can_construct(target: str, word_bank: list[str]) -> bool:
    dp = [False] * (len(target) + 1)
    dp[0] = True

    for i in range(len(target) + 1):
        if dp[i]:
            for word in word_bank:
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] = True

    return dp[len(target)]


def main():
    towels, designs = read_towels_and_designs(Path("input.txt"))
    print(sum([1 for design in designs if can_construct(design, towels)]))


if __name__ == '__main__':
    main()
