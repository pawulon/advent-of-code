from pathlib import Path
from day_13_1 import read_machines, count_tokens, NoSolution


def main():
    machines = read_machines(Path("input.txt"), prize_position_correction=10000000000000)
    token_counts = 0
    for machine in machines:
        try:
            result = machine.solve()
            token_counts += count_tokens(result)
        except NoSolution:
            continue
    print(token_counts)


if __name__ == '__main__':
    main()
