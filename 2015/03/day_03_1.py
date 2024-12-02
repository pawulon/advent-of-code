from pathlib import Path
from typing import List, Tuple


def read_directions(input_path: Path) -> List[str]:
    return list(input_path.read_text())

def get_moves(directions: List[str]) -> List[Tuple[int, int]]:
    moves = [(0, 0)]
    for direction in directions:
        match direction:
            case "^":
                moves.append((moves[-1][0], moves[-1][1] + 1))
            case ">":
                moves.append((moves[-1][0] + 1, moves[-1][1]))
            case "v":
                moves.append((moves[-1][0], moves[-1][1] - 1))
            case "<":
                moves.append((moves[-1][0] - 1, moves[-1][1]))
    return moves

def main():
    directions = read_directions(Path("input.txt"))
    moves = get_moves(directions)
    unique_houses_locations = set(moves)
    print(len(unique_houses_locations))


if __name__ == '__main__':
    main()
