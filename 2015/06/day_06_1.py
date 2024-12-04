from enum import Enum
from pathlib import Path


class ActionType(Enum):
    TURN_OFF = 0
    TURN_ON = 1
    TOGGLE = 2


Point = tuple[int, int]
Action = (ActionType, Point, Point)


def read_actions(input_path: Path) -> list[Action]:
    input_lines = input_path.read_text().split('\n')
    actions = []
    for line in input_lines:
        left, right = line.split("through")
        if left.startswith("turn on"):
            action = ActionType.TURN_ON
        elif left.startswith("turn off"):
            action = ActionType.TURN_OFF
        else:
            action = ActionType.TOGGLE
        left_split = left.split()
        right_split = right.split()
        left_corner = left_split[-1].split(',')
        left_corner = int(left_corner[0]), int(left_corner[1])
        right_corner = right_split[-1].split(',')
        right_corner = int(right_corner[0]), int(right_corner[1])
        actions.append((action, left_corner, right_corner))
    return actions


def get_lights(left_corner: Point, right_corner: Point) -> list[Point]:
    points = []
    for i in range(left_corner[0], right_corner[0] + 1):
        for j in range(left_corner[1], right_corner[1] + 1):
            points.append((i, j))
    return points


def execute_action(all_the_lights: set[Point], action_type: ActionType, actionable_lights: list[Point]) -> None:
    if action_type == ActionType.TURN_ON:
        for light in actionable_lights:
            all_the_lights.add(light)
    elif action_type == ActionType.TURN_OFF:
        for light in actionable_lights:
            if light in all_the_lights:
                all_the_lights.remove(light)
    else:
        for light in actionable_lights:
            if light in all_the_lights:
                all_the_lights.remove(light)
            else:
                all_the_lights.add(light)


def main():
    actions = read_actions(Path("input.txt"))
    all_the_lights: set[Point] = set()
    for action in actions:
        lights = get_lights(action[1], action[2])
        execute_action(all_the_lights, action[0], lights)
    print(all_the_lights)
    print(len(all_the_lights))


if __name__ == '__main__':
    main()
