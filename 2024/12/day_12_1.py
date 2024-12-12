from collections import namedtuple
from copy import deepcopy
from pathlib import Path

Map = list[list[str]]
Point = namedtuple("Point", ("x", "y"))


def get_potential_neighbour_points(point: Point) -> list[Point]:
    top_point = Point(point.x, point.y - 1)
    right_point = Point(point.x + 1, point.y)
    left_point = Point(point.x - 1, point.y)
    bottom_point = Point(point.x, point.y + 1)
    return [top_point, right_point, left_point, bottom_point]


class Garden:
    def __init__(self, plant_map: Map):
        self.plant_map = plant_map
        self.max_x = len(self.plant_map[0])
        self.max_y = len(self.plant_map)

    def plant_at_point(self, point: Point) -> str:
        return self.plant_map[point.y][point.x]

    def erase_plant(self, point: Point) -> None:
        self.plant_map[point.y][point.x] = "@"

    def read_regions(self) -> list[list[Point]]:
        plant_map_copy = deepcopy(self.plant_map)
        regions = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                point = Point(x, y)
                if self.plant_at_point(point) == "@":
                    continue
                regions.append(self.get_region_plants(point))
        self.plant_map = plant_map_copy
        return regions

    def count_neighbors(self, point: Point) -> int:
        potential_neighbours = get_potential_neighbour_points(point)
        count = 0
        for potential_point in potential_neighbours:
            if not self.is_point_out_of_map(potential_point) and self.plant_at_point(point) == self.plant_at_point(
                    potential_point):
                count += 1
        return count

    def get_region_plants(self, point: Point) -> list[Point]:
        if self.plant_at_point(point) == "@":
            return []
        potential_points = get_potential_neighbour_points(point)
        region_plants = []
        neighbour_plants = []
        for potential_point in potential_points:
            if not self.is_point_out_of_map(potential_point) and self.plant_at_point(point) == self.plant_at_point(
                    potential_point):
                neighbour_plants.append(potential_point)
        self.erase_plant(point)
        for neighbour_plant in neighbour_plants:
            region_plants += self.get_region_plants(neighbour_plant)
        region_plants.append(point)
        return region_plants

    def is_point_out_of_map(self, point: Point) -> bool:
        return not (0 <= point.x < self.max_x and 0 <= point.y < self.max_y)


def read_garden(input_path: Path) -> Garden:
    return Garden([list(line) for line in input_path.read_text().splitlines()])


def calculate_region_area(region: list[Point]) -> int:
    return len(region)


def calculate_region_perimeter(region: list[Point], garden: Garden) -> int:
    perimeter = 0
    for plant in region:
        perimeter += 4 - garden.count_neighbors(plant)
    return perimeter


def main():
    garden = read_garden(Path("input.txt"))
    regions = garden.read_regions()
    print(sum([calculate_region_area(region) * calculate_region_perimeter(region, garden) for region in regions]))

if __name__ == '__main__':
    main()
