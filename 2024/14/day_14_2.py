import os
from pathlib import Path
from day_14_1 import read_robots, Robot, MAX_Y, MAX_X

def is_potential_tree(robots: list[Robot]) -> bool:
    left_side = len([robot for robot in robots if robot.p.x < MAX_X // 3])
    middle = len([robot for robot in robots if MAX_X // 3 < robot.p.x < 2* MAX_X // 3])
    right_side = len([robot for robot in robots if robot.p.x > 2 * MAX_X // 3])
    return left_side + right_side < middle

def print_robots(robots: list[Robot], iteration: int) -> None:
    if not is_potential_tree(robots):
        return
    robot_points = set([(robot.p.x, robot.p.y) for robot in robots])
    for y in range(MAX_Y):
        line = ""
        for x in range(MAX_X):
            if (x, y) in robot_points:
                line += "X"
            else:
                line += "."
        print(line)
    input(f"Iteration: {iteration}")
    clear_console()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    robots = read_robots(Path("input.txt"))
    iteration = 1
    while True:
        for robot in robots:
            robot.move(1)

        print_robots(robots, iteration)
        iteration += 1

if __name__ == '__main__':
    main()
