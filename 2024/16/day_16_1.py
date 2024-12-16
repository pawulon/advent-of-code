import heapq
from collections import namedtuple
from pathlib import Path

Point = namedtuple("Point", ["x", "y"])
Map = list[list[str]]

PointInfo = namedtuple("PointInfo", ["point", "path"])


def read_maze_map(input_path: Path) -> Map:
    lines = input_path.read_text().splitlines()
    return [list(line) for line in lines]


class Maze:
    def __init__(self, maze_map: Map):
        self.map = maze_map
        self.max_y = len(self.map)
        self.max_x = len(self.map[0])
        self.start = self.find_start()
        self.end = self.find_end()
        self.path_to_point: dict[Point, list[Point]] = {self.start: []}

    def print_maze(self, path: list[Point] = None):
        for y in range(self.max_y):
            line = ""
            for x in range(self.max_x):
                if path and Point(x, y) in path:
                    line += "X"
                else:
                    line += self.map[y][x]
            print(line)
        print()

    def find_start(self) -> Point:
        return self.find_letter("S")

    def find_end(self) -> Point:
        return self.find_letter("E")

    def find_letter(self, letter: str) -> Point:
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.map[y][x] == letter:
                    return Point(x, y)

    def get_letter_at(self, point: Point) -> str:
        return self.map[point.y][point.x]

    def get_available_steps(self, point: Point) -> list[Point]:
        available_steps = []
        px, py = point
        for point in [Point(px + 1, py), Point(px - 1, py), Point(px, py - 1), Point(px, py + 1)]:
            if self.get_letter_at(point) != "#":
                available_steps.append(point)
        return available_steps

    def find_lowest_score(self) -> tuple[int, list[Point], dict[Point, list[list[Point]]]]:
        points: dict[Point, tuple[int, list[Point]]] = {self.start: (0, [])}
        points_other_paths: dict[Point, list[list[Point]]] = {}
        priority_queue = []
        heapq.heappush(priority_queue, (0, PointInfo(point=self.start, path=[])))

        while priority_queue:
            priority, point_info = heapq.heappop(priority_queue)
            point = point_info.point
            path = point_info.path
            if path:
                direction = self.find_direction(path[-1], point)
            else:
                direction = (1, 0)
            if point == self.find_end():
                return priority, path, points_other_paths

            available_steps = self.get_available_steps(point)
            for available_step in available_steps:
                if available_step in path:
                    continue
                score = 0
                new_direction = self.find_direction(point, available_step)
                if new_direction != direction:
                    score = 1000
                new_path = path + [point]
                new_score = priority + score + 1
                if available_step in points:
                    if points[available_step][0] < new_score:
                        if new_score - points[available_step][0] == 1000:
                            current_path_direction = self.find_direction(points[available_step][1][-1], available_step)
                            next_point = Point(x=available_step.x + current_path_direction.x,
                                               y=available_step.y + current_path_direction.y)
                            if self.get_letter_at(next_point) == "#":
                                if available_step in points_other_paths:
                                    points_other_paths[available_step].append(new_path)
                                else:
                                    points_other_paths[available_step] = [new_path]
                        continue
                    elif points[available_step][0] == new_score:
                        if available_step in points_other_paths:
                            points_other_paths[available_step].append(points[available_step][1])
                        else:
                            points_other_paths[available_step] = [points[available_step][1]]
                    elif points[available_step][0] > new_score:
                        points_other_paths[available_step] = []
                points[available_step] = (new_score, new_path)
                heapq.heappush(priority_queue, (new_score, PointInfo(available_step, new_path)))

        raise ValueError("hę?")

    def find_direction(self, point_a: Point, point_b: Point) -> Point:
        return Point(point_b.x - point_a.x, point_b.y - point_a.y)


def main():
    maze_map = read_maze_map(Path("input.txt"))
    maze = Maze(maze_map)
    score, _, _ = maze.find_lowest_score()
    print(score)


if __name__ == '__main__':
    main()
