from collections import namedtuple
from pathlib import Path

Map = list[list[int]]
Point = namedtuple("Point", ["x", "y"])


def read_map_heights(file_path: Path) -> Map:
    lines = Path(file_path).read_text().splitlines()
    return [list(map(int, list(line))) for line in lines]


class TopoMap:
    def __init__(self, heights: Map):
        self.heights = heights
        self.max_y = len(self.heights)
        self.max_x = len(self.heights[0])

    def find_trail_heads(self) -> list[Point]:
        trail_heads = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.heights[y][x] == 0:
                    trail_heads.append(Point(x=x, y=y))
        return trail_heads

    def height_at_point(self, point: Point) -> int:
        return self.heights[point.y][point.x]

    def get_possible_top_points(self, point: Point) -> set[Point]:
        top_points: set[Point] = set()
        if self.height_at_point(point) == 8:
            return set(self.get_hikable_points(point))
        else:
            hikable_points = self.get_hikable_points(point)
            for point in hikable_points:
                top_points.update(self.get_possible_top_points(point))
        return top_points

    def get_hikable_points(self, point: Point) -> list[Point]:
        x = point.x
        y = point.y
        left_point = Point(x + 1, y)
        right_point = Point(x - 1, y)
        up_point = Point(x, y - 1)
        down_point = Point(x, y + 1)
        current_height = self.height_at_point(point)
        potential_hikes = [left_point, right_point, up_point, down_point]
        return [point for point in potential_hikes if
                self.is_point_inside_map(point) and self.height_at_point(point) - 1 == current_height]

    def is_point_inside_map(self, point: Point) -> bool:
        return 0 <= point.x < self.max_x and 0 <= point.y < self.max_y


def main():
    heights = read_map_heights(Path("input.txt"))
    topo_map = TopoMap(heights=heights)
    trail_heads = topo_map.find_trail_heads()
    print(sum([len(topo_map.get_possible_top_points(trail_head)) for trail_head in trail_heads]))


if __name__ == '__main__':
    main()
