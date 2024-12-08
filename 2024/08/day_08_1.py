from collections import namedtuple
from itertools import combinations
from pathlib import Path

Map = list[list[str]]
Point = namedtuple('Point', ['x', 'y'])
AntennasPositions = dict[str, list[Point]]


def read_map(input_path: Path) -> list[list[str]]:
    lines = input_path.read_text().splitlines()
    return [list(line) for line in lines]


def read_antennas_locations(antenna_map: Map) -> AntennasPositions:
    antennas_positions = {}
    for y in range(len(antenna_map)):
        for x in range(len(antenna_map[0])):
            if antenna_map[y][x] != '.':
                antennas_positions.setdefault(antenna_map[y][x], []).append(Point(x=x, y=y))
    return antennas_positions


def find_antinodes_positions(antennas_position: AntennasPositions,
                             map_width: int, map_height: int,
                             with_resonant_harmonics: bool = False) -> list[Point]:
    antinodes = []
    for antenna_positions in antennas_position.values():
        if len(antenna_positions) < 2:
            raise ValueError("Only one antenna?")
        point_pairs = get_all_points_pairs(antenna_positions)
        antinodes += find_antinodes_for_all_pairs(point_pairs, map_width, map_height, with_resonant_harmonics)
    return list(set(antinodes))


def find_antinodes_for_all_pairs(point_pairs: list[tuple[Point, Point]],
                                 max_x: int, max_y: int,
                                 with_resonant_harmonics: bool) -> list[Point]:
    antinodes = []
    for point_pair in point_pairs:
        point_a, point_b = point_pair
        if with_resonant_harmonics:
            antinodes += find_antinodes_for_two_points_with_resonant_harmonics(point_a, point_b, max_x, max_y)
        else:
            antinodes += find_antinodes_for_two_points(point_a, point_b, max_x, max_y)
    return antinodes


def find_antinodes_for_two_points(point_a: Point, point_b: Point, max_x: int, max_y: int) -> list[Point]:
    vector = get_vector_between_two_points(point_a, point_b)
    reversed_vector = reverse_vector(vector)
    antinodes = []

    for point in [move_point_by_vector(point_b, vector), move_point_by_vector(point_a, reversed_vector)]:
        if not is_point_out_of_map(point, max_x, max_y):
            antinodes.append(point)
    return antinodes


def find_antinodes_for_two_points_with_resonant_harmonics(point_a: Point, point_b: Point,
                                                          max_x: int, max_y: int) -> list[Point]:
    vector = get_vector_between_two_points(point_a, point_b)
    reversed_vector = reverse_vector(vector)
    point_a_antinodes = move_point_by_vector_with_resonant_harmonics(point_a, vector, max_x, max_y)
    point_b_antinodes = move_point_by_vector_with_resonant_harmonics(point_b, reversed_vector, max_x, max_y)

    return point_a_antinodes + point_b_antinodes


def move_point_by_vector_with_resonant_harmonics(point: Point, vector: Point, max_x: int, max_y: int) -> list[Point]:
    antinodes = []
    point = move_point_by_vector(point, vector)
    while not is_point_out_of_map(point, max_x, max_y):
        antinodes.append(point)
        point = move_point_by_vector(point, vector)
    return antinodes


def get_vector_between_two_points(point_a: Point, point_b: Point) -> Point:
    return Point(x=point_b.x - point_a.x, y=point_b.y - point_a.y)


def move_point_by_vector(point: Point, vector: Point) -> Point:
    return Point(x=point.x + vector.x, y=point.y + vector.y)


def reverse_vector(vector: Point) -> Point:
    return Point(x=-1 * vector.x, y=-1 * vector.y)


def get_all_points_pairs(points: list[Point]) -> list[tuple[Point, Point]]:
    return list(combinations(points, 2))


def is_point_out_of_map(point: Point, max_x: int, max_y: int) -> bool:
    return not (0 <= point.x < max_x and 0 <= point.y < max_y)


def main():
    antenna_map = read_map(Path("input.txt"))
    antennas_positions = read_antennas_locations(antenna_map)
    antinodes = find_antinodes_positions(antennas_positions, map_width=len(antenna_map[0]), map_height=len(antenna_map))
    print(len(antinodes))


if __name__ == '__main__':
    main()
