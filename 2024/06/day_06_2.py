import copy
from pathlib import Path
from day_06_1 import read_lab_map, track_the_guard, Map, Steps, Point, find_the_guard, GuardLoopException


def find_obstructions_causing_loop(lab_map: Map, steps: Steps) -> list[Point]:
    obstructions = []
    excluded_point = find_the_guard(lab_map)
    for point in steps.keys():
        if point == excluded_point:
            continue
        new_steps = {}
        new_map = copy.deepcopy(lab_map)
        new_map[point.y][point.x] = '#'
        try:
            track_the_guard(new_map, new_steps)
        except GuardLoopException:
            obstructions.append(point)
    return obstructions


def have_common_element(list1: list, list2: list) -> bool:
    return bool(set(list1) & set(list2))


def main():
    lab_map = read_lab_map(Path("input.txt"))
    lab_map_copy = copy.deepcopy(lab_map)
    steps = {}
    track_the_guard(lab_map, steps)
    obstructions = find_obstructions_causing_loop(lab_map_copy, steps)
    print(len(obstructions))


if __name__ == '__main__':
    main()
