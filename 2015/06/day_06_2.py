from collections import defaultdict
from pathlib import Path
from day_06_1 import read_actions, get_lights, Point, ActionType


def execute_action(all_the_lights: dict[Point, int], action_type: ActionType, actionable_lights: list[Point]) -> None:
    if action_type == ActionType.TURN_ON:
        for light in actionable_lights:
            all_the_lights[light] += 1
    elif action_type == ActionType.TURN_OFF:
        for light in actionable_lights:
            if light in all_the_lights and all_the_lights[light] > 0:
                all_the_lights[light] -= 1
    else:
        for light in actionable_lights:
            all_the_lights[light] += 2


def main():
    actions = read_actions(Path("input.txt"))
    all_the_lights: dict[Point, int] = defaultdict(int)
    for action in actions:
        lights = get_lights(action[1], action[2])
        execute_action(all_the_lights, action[0], lights)
    total_brightness = sum([value for value in all_the_lights.values()])
    print(total_brightness)


if __name__ == '__main__':
    main()
