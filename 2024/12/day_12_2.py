from pathlib import Path
from day_12_1 import read_garden, Point, calculate_region_area


def count_region_sides(region: list[Point]) -> int:
    count = 0
    vertices = get_all_region_vertices(region)
    for vertex in set(vertices):
        if vertices.count(vertex) in (1, 3):
            count += 1
    count += count_corners(region)
    return count


def count_corners(region: list[Point]) -> int:
    count = 0
    for point in region:
        count += count_point_corner(point, region)
    return count


def count_point_corner(point: Point, region: list[Point]) -> int:
    top_left = Point(point.x - 1, point.y - 1)
    top = Point(point.x, point.y - 1)
    top_right = Point(point.x + 1, point.y - 1)
    left = Point(point.x - 1, point.y)
    right = Point(point.x + 1, point.y)
    bottom_left = Point(point.x - 1, point.y + 1)
    bottom = Point(point.x, point.y + 1)
    bottom_right = Point(point.x + 1, point.y + 1)
    count = 0
    if top_left in region and top not in region and left not in region:
        count += 1
    if top_right in region and top not in region and right not in region:
        count += 1
    if bottom_left in region and left not in region and bottom not in region:
        count += 1
    if bottom_right in region and right not in region and bottom not in region:
        count += 1
    return count


def get_all_region_vertices(region: list[Point]) -> list[Point]:
    points = []
    for point in region:
        points += list(get_point_vertices(point))
    return points


def get_point_vertices(point: Point) -> tuple[Point, Point, Point, Point]:
    double_point = Point(point.x * 2, point.y * 2)
    top_left = Point(double_point.x - 1, double_point.y - 1)
    top_right = Point(double_point.x + 1, double_point.y - 1)
    bottom_left = Point(double_point.x - 1, double_point.y + 1)
    bottom_right = Point(double_point.x + 1, double_point.y + 1)
    return top_left, top_right, bottom_left, bottom_right


def main():
    garden = read_garden(Path("input.txt"))
    regions = garden.read_regions()
    # for region in regions:
    #     print(count_region_sides(region))
    #     print(calculate_region_area(region))
    #     print(count_region_sides(region) * calculate_region_area(region))

    print(sum([count_region_sides(region) * calculate_region_area(region) for region in regions]))


if __name__ == '__main__':
    main()
