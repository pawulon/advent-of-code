import operator
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

MAX_X = 101
MAX_Y = 103


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Robot:
    p: Point
    v: Point

    def move(self, number_of_iterations) -> None:
        for _ in range(number_of_iterations):
            self.p = Point(self.p.x + self.v.x, self.p.y + self.v.y)
            self.bathromize()

    def bathromize(self) -> None:
        x = self.p.x
        y = self.p.y
        if x < 0:
            x = MAX_X - (abs(x) % MAX_X)
        elif x >= MAX_X:
            x = x % MAX_X

        if y < 0:
            y = MAX_Y - (abs(y) % MAX_Y)
        elif y >= MAX_Y:
            y = y % MAX_Y
        self.p = Point(x, y)


def read_robots(input_path: Path) -> list[Robot]:
    return [parse_robot(line) for line in input_path.read_text().splitlines()]


def parse_robot(line: str) -> Robot:
    p, v = line.split()
    px, py = p.split("=")[1].split(",")
    vx, vy = v.split("=")[1].split(",")
    return Robot(p=Point(int(px), int(py)), v=Point(int(vx), int(vy)))


def calculate_safety_factor(robots: list[Robot]) -> int:
    first_quadrant = [robot for robot in robots if robot.p.x < MAX_X // 2 and robot.p.y < MAX_Y // 2]
    print(len(first_quadrant), first_quadrant)
    second_quadrant = [robot for robot in robots if robot.p.x > MAX_X // 2 and robot.p.y < MAX_Y // 2]
    print(len(second_quadrant), second_quadrant)
    third_quadrant = [robot for robot in robots if robot.p.x > MAX_X // 2 and robot.p.y > MAX_Y // 2]
    print(len(third_quadrant), third_quadrant)
    forth_quadrant = [robot for robot in robots if robot.p.x < MAX_X // 2 and robot.p.y > MAX_Y // 2]
    print(len(forth_quadrant), forth_quadrant)
    return reduce(operator.mul, [len(first_quadrant), len(second_quadrant),
                                 len(third_quadrant), len(forth_quadrant)])


def print_robots(robots: list[Robot]) -> None:
    robot_points = set([robot.p for robot in robots])
    for y in range(MAX_Y):
        line = ""
        for x in range(MAX_X):
            if Point(x, y) in robot_points:
                line += "X"
            else:
                line += "."
        print(line)
    a = 2


def main():
    robots = read_robots(Path("input.txt"))
    for robot in robots:
        robot.move(100)
    print(robots)
    print(calculate_safety_factor(robots))


if __name__ == '__main__':
    main()
