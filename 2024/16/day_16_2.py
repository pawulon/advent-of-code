from pathlib import Path
from day_16_1 import read_maze_map, Maze


def main():
    maze_map = read_maze_map(Path("input.txt"))
    maze = Maze(maze_map)
    _, path, other_paths = maze.find_lowest_score()
    other_points_in_path = []
    for key in other_paths.keys():
        if key in path:
            other_points_in_path += [point for path in other_paths[key] for point in path]
    for key in other_paths.keys():
        if key not in path and key in other_points_in_path:
            other_points_in_path += [point for path in other_paths[key] for point in path]
    print(len(set(path + other_points_in_path + [maze.end])))


if __name__ == '__main__':
    main()
