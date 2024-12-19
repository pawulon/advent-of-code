from pathlib import Path
from day_19_1 import read_towels_and_designs


def count_construct(target: str, word_bank: list[str]) -> int:
    dp = [0] * (len(target) + 1)
    dp[0] = 1

    for i in range(len(target) + 1):
        if dp[i] != 0:
            for word in word_bank:
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] += dp[i]

    return dp[len(target)]


def main():
    towels, designs = read_towels_and_designs(Path("input.txt"))
    print(sum([count_construct(design, towels) for design in designs]))


if __name__ == '__main__':
    main()
