from collections import namedtuple
from itertools import cycle, count
from pathlib import Path
from typing import Iterator

Map = list[list[str]]
Point = namedtuple('Point', ['x', 'y'])
Steps = dict[Point, list[Point]]


class GuardLoopException(Exception):
    pass


def read_lab_map(input_path: Path) -> Map:
    lines = input_path.read_text().splitlines()
    return [list(line) for line in lines]


def track_the_guard(lab_map: Map, steps: Steps = None, debug=False) -> None:
    guard = find_the_guard(lab_map)
    directions: Iterator[Point] = cycle([Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)])
    direction = next(directions)
    while not is_guard_out_of_map(guard, lab_map):
        old_position = guard
        guard, direction = move_guard_by_one_step(guard=guard, direction=direction, directions=directions,
                                                  lab_map=lab_map)
        if steps is not None:
            steps.setdefault(old_position, []).append(guard)
            if has_duplicate(steps[old_position]):
                raise GuardLoopException
        if debug:
            print_lab_map(lab_map)


def has_duplicate(collection: list) -> bool:
    return len(collection) != len(set(collection))


def find_the_guard(lab_map: Map) -> Point:
    for y in range(len(lab_map)):
        for x in range(len(lab_map[y])):
            if lab_map[y][x] == '^':
                return Point(x, y)
    raise RuntimeError("Guard is not there")


def is_guard_out_of_map(guard: Point, lab_map: Map) -> bool:
    return not (0 <= guard.x < len(lab_map[0]) and 0 <= guard.y < len(lab_map))


def move_guard_by_one_step(guard: Point, direction: Point, directions: Iterator[Point], lab_map: Map) -> tuple[
    Point, Point]:
    next_step = Point(guard.x + direction.x, guard.y + direction.y)
    if not is_guard_out_of_map(next_step, lab_map):
        while is_guard_blocked(next_step, lab_map):
            direction = next(directions)
            next_step = Point(guard.x + direction.x, guard.y + direction.y)
    mark_guard_position(guard, lab_map)
    return next_step, direction


def is_guard_blocked(guard: Point, lab_map: Map) -> bool:
    return lab_map[guard.y][guard.x] == '#'


def mark_guard_position(guard: Point, lab_map: Map) -> None:
    lab_map[guard.y][guard.x] = 'X'


def print_lab_map(lab_map: Map) -> None:
    for line in lab_map:
        print(''.join(line))
    print()


def count_visited_positions(lab_map: Map) -> int:
    position_count = 0
    for line in lab_map:
        for field in line:
            if field == 'X':
                position_count += 1
    return position_count


def main():
    lab_map = read_lab_map(Path("input.txt"))
    track_the_guard(lab_map)
    print(count_visited_positions(lab_map))


if __name__ == '__main__':
    main()
