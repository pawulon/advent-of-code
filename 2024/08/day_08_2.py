from pathlib import Path
from day_08_1 import read_map, read_antennas_locations, find_antinodes_positions


def main():
    antenna_map = read_map(Path("input.txt"))
    antennas_positions = read_antennas_locations(antenna_map)
    antinodes = find_antinodes_positions(antennas_positions,
                                         map_width=len(antenna_map[0]), map_height=len(antenna_map),
                                         with_resonant_harmonics=True)
    print(len(antinodes))


if __name__ == '__main__':
    main()
