from dataclasses import dataclass
from pathlib import Path


class NoSolution(Exception):
    pass


@dataclass
class Machine:
    a1: int
    b1: int
    c1: int
    a2: int
    b2: int
    c2: int
    prize_position_correction: int = 0

    def __post_init__(self):
        self.c1 = self.c1 + self.prize_position_correction
        self.c2 = self.c2 + self.prize_position_correction

    @property
    def w(self) -> int:
        return self.a1 * self.b2 - self.b1 * self.a2

    @property
    def wx(self) -> int:
        return self.c1 * self.b2 - self.b1 * self.c2

    @property
    def wy(self) -> int:
        return self.a1 * self.c2 - self.c1 * self.a2

    def solve(self) -> tuple[int, int]:
        w = self.w
        wx = self.wx
        wy = self.wy
        if w == 0:
            raise ValueError("W == 0 AAAAA")
        if self.wx % self.w != 0 or self.wy % self.w != 0:
            raise NoSolution

        x = int(wx / w)
        y = int(wy / w)
        return x, y


def read_machines(input_path: Path, prize_position_correction: int = 0) -> list[Machine]:
    lines = iter(input_path.read_text().splitlines())
    machines = []
    try:
        while True:
            line_1 = next(lines)
            a1, a2 = read_button(line_1)
            line_2 = next(lines)
            b1, b2 = read_button(line_2)
            line_3 = next(lines)
            c1, c2 = read_prize(line_3)
            machines.append(
                Machine(a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, prize_position_correction=prize_position_correction))
            next(lines)  # empty line
    except StopIteration:
        return machines


def read_prize(line: str) -> tuple[int, int]:
    line_split = line.split("=")
    c1 = int(line_split[1].split(",")[0])
    c2 = int(line_split[-1])
    return c1, c2


def read_button(line: str) -> tuple[int, int]:
    line_split = line.split("+")
    a = int(line_split[1].split(",")[0])
    b = int(line_split[-1])
    return a, b


def count_tokens(result: tuple[int, int]) -> int:
    return result[0] * 3 + result[1]


def main():
    machines = read_machines(Path("input.txt"))
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
