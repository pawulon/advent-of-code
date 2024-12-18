from pathlib import Path
from day_18_1 import read_byte_positions, Memory, Point

def main():
    byte_positions = read_byte_positions(Path("input.txt"))
    size = 71
    memory = Memory(byte_positions, size)
    for i in range(1024, len(byte_positions)):
        memory.simulate(i)
        path = memory.find_shortest_path(Point(0, 0), Point(size - 1, size - 1))
        if path is None:
            print(byte_positions[i])
            break


if __name__ == '__main__':
    main()
