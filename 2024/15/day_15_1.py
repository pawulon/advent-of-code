from collections import namedtuple
from copy import deepcopy
from pathlib import Path

Map = list[list[str]]
Point = namedtuple("Point", ("x", "y"))



def read_map_and_moves(input_path: Path) -> tuple[Map, list[str]]:
    lines = input_path.read_text().splitlines()
    warehouse_map = []
    moves = []
    is_that_a_map = True
    for line in lines:
        if not line:
            is_that_a_map = False
            continue
        if is_that_a_map:
            warehouse_map.append(list(line))
        else:
            moves += list(line)

    return warehouse_map, moves


class Warehouse:
    def __init__(self, warehouse_map: Map, robot_moves: list[str]):
        self.map = warehouse_map
        self.max_y = len(self.map)
        self.max_x = len(self.map[0])
        self.moves = robot_moves
        self.robot = self.find_robot()

    def print_map(self):
        for line in self.map:
            print("".join(line))
        print()

    def find_robot(self) -> Point:
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.map[y][x] == "@":
                    return Point(x, y)

    def whats_at(self, point: Point) -> str:
        return self.map[point.y][point.x]

    def update_map(self, point: Point, new_value: str) -> None:
        self.map[point.y][point.x] = new_value

    def move_robot(self) -> None:
        for move in self.moves:
            vector = self.get_vector_of_movement(move=move)
            new_point = self.new_point(self.robot, vector)
            if self.whats_at(new_point) == "#":
                continue
            if self.whats_at(new_point) == "O":
                self.move_box(new_point, vector)
            if self.whats_at(new_point) in ["[", "]"]:
                self.move_big_box(new_point, vector)
            if self.whats_at(new_point) == ".":
                self.update_map(self.robot, ".")
                self.update_map(new_point, "@")
                self.robot = new_point

    def move_box(self, point: Point, direction: Point) -> None:
        new_point = self.new_point(point, direction)
        if self.whats_at(new_point) == "#":
            return
        if self.whats_at(new_point) == "O":
            self.move_box(new_point, direction)
        if self.whats_at(new_point) == ".":
            self.update_map(point, ".")
            self.update_map(new_point, "O")

    def move_big_box(self, point: Point, direction: Point) -> None:
        if self.whats_at(point) == "[":
            left_side = point
            right_side = Point(point.x + 1, point.y)
        else:
            left_side = Point(point.x - 1, point.y)
            right_side = point

        if direction == (-1, 0):
            new_point = self.new_point(left_side, direction)
            if self.whats_at(new_point) == "#":
                return
            if self.whats_at(new_point) in ["[", "]"]:
                self.move_big_box(new_point, direction)
            if self.whats_at(new_point) == ".":
                self.update_map(new_point, "[")
                self.update_map(left_side, "]")
                self.update_map(point, ".")

        if direction == (1, 0):
            new_point = self.new_point(right_side, direction)
            if self.whats_at(new_point) == "#":
                return
            if self.whats_at(new_point) in ["[", "]"]:
                self.move_big_box(new_point, direction)
            if self.whats_at(new_point) == ".":
                self.update_map(new_point, "]")
                self.update_map(right_side, "[")
                self.update_map(point, ".")

        if direction == (0, -1) or direction == (0, 1):
            new_right_point = self.new_point(right_side, direction)
            new_left_point = self.new_point(left_side, direction)
            if self.whats_at(new_right_point) == "#" or self.whats_at(new_left_point) == "#":
                return
            if self.whats_at(new_right_point) == "]":
                self.move_big_box(new_right_point, direction)
            if self.whats_at(new_right_point) == "[":
                if self.whats_at(new_left_point) == "]":
                    saved_map = deepcopy(self.map)
                    self.move_big_box(new_left_point, direction)
                    self.move_big_box(new_right_point, direction)
                    if self.whats_at(new_left_point) != "." or self.whats_at(new_right_point) != ".":
                        self.map = saved_map
                else:
                    self.move_big_box(new_right_point, direction)
            elif self.whats_at(new_left_point) == "]":
                self.move_big_box(new_left_point, direction)
            if self.whats_at(new_left_point) == "." and self.whats_at(new_right_point) == ".":
                self.update_map(new_left_point, "[")
                self.update_map(new_right_point, "]")
                self.update_map(left_side, ".")
                self.update_map(right_side, ".")

    def find_big_box_second_part(self, point: Point):
        if self.whats_at(point) == "[":
            return Point(point.x + 1, point.y)
        return Point(point.x - 1, point.y)

    def get_sum_of_boxes_gps(self, big_box: bool = False) -> int:
        boxes = self.find_boxes(big_box=big_box)
        gps_sum = 0
        for box in boxes:
            gps_sum += self.get_gps_of_box(box)
        return gps_sum

    def get_gps_of_box(self, box: Point) -> int:
        return 100 * box.y + box.x

    def find_boxes(self, big_box: bool = False) -> list[Point]:
        if big_box:
            box = "["
        else:
            box = "O"
        boxes = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.map[y][x] == box:
                    boxes.append(Point(x, y))
        return boxes

    def new_point(self, point: Point, vector: Point) -> Point:
        return Point(x=point.x + vector.x, y=point.y + vector.y)

    def get_vector_of_movement(self, move: str) -> Point:
        if move == "^":
            return Point(0, -1)
        if move == ">":
            return Point(1, 0)
        if move == "v":
            return Point(0, 1)
        if move == "<":
            return Point(-1, 0)


def main():
    warehouse_map, moves = read_map_and_moves(Path("input.txt"))
    warehouse = Warehouse(warehouse_map, moves)
    warehouse.move_robot()
    print(warehouse.get_sum_of_boxes_gps())


if __name__ == '__main__':
    main()
