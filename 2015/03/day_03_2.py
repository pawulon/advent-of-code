from pathlib import Path
from day_03_1 import read_directions, get_moves


def main():
    directions = read_directions(Path("input.txt"))
    santa_directions = directions[0:-1:2]
    robo_santa_directions = directions[1:-1:2]
    santa_moves = get_moves(santa_directions)
    robo_santa_moves = get_moves(robo_santa_directions)
    unique_houses_locations = set(santa_moves) | set(robo_santa_moves)
    print(len(unique_houses_locations))


if __name__ == '__main__':
    main()
