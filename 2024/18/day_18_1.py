import heapq
from collections import namedtuple
from pathlib import Path

Point = namedtuple("Point", ["x", "y"])


def read_byte_positions(input_path: Path) -> list[Point]:
    lines = input_path.read_text().splitlines()
    positions = []
    for line in lines:
        x, y = line.split(",")
        positions.append(Point(int(x), int(y)))
    return positions


class Memory:
    def __init__(self, byte_positons: list[Point], size: int):
        self.bytes = byte_positons
        self.size = size
        self.grid = []

    def simulate(self, number_of_bytes: int):
        self.grid = []
        for y in range(self.size):
            line = []
            for x in range(self.size):
                if Point(x, y) in self.bytes[:number_of_bytes + 1]:
                    line.append("#")
                else:
                    line.append(".")
            self.grid.append(line)

    def print(self, path: list[Point]):
        for y in range(self.size):
            line = ""
            for x in range(self.size):
                if path and Point(x, y) in path:
                    line += "O"
                else:
                    line += self.grid[y][x]
            print(line)
        print()

    def find_shortest_path(self, start: Point, end: Point) -> list[Point]:
        points: dict[Point, list[Point]] = {start: []}
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        while priority_queue:
            # print(priority_queue)
            priority, point = heapq.heappop(priority_queue)
            path = points[point]

            if point == Point(18, 18):
                a = 2

            if point == end:
                return path

            available_steps = self.get_available_steps(point)
            for available_step in available_steps:
                if available_step in path:
                    continue
                new_path = path + [point]
                new_priority = len(new_path) + get_distance(available_step, end)
                if available_step in points:
                    if len(points[available_step]) < len(new_path):
                        points[available_step] = new_path
                    else:
                        continue
                else:
                    points[available_step] = new_path
                heapq.heappush(priority_queue, (new_priority, available_step))

    def get_available_steps(self, point: Point) -> list[Point]:
        available_steps = []
        px, py = point
        for point in [Point(px + 1, py), Point(px - 1, py), Point(px, py - 1), Point(px, py + 1)]:
            if 0 <= point.x < self.size and 0 <= point.y < self.size and self.grid[point.y][point.x] != "#":
                available_steps.append(point)
        return available_steps


def get_distance(a: Point, b: Point) -> int:
    return b.x - a.x + b.y - a.y


def main():
    byte_positions = read_byte_positions(Path("input.txt"))
    memory = Memory(byte_positions, 71)
    memory.simulate(1024)
    path = memory.find_shortest_path(Point(0, 0), Point(70, 70))
    print(len(path))


if __name__ == '__main__':
    main()
