from pathlib import Path
from day_10_1 import read_map_heights, TopoMap


def main():
    heights = read_map_heights(Path("input.txt"))
    topo_map = TopoMap(heights=heights)
    trail_heads = topo_map.find_trail_heads()
    print(sum([len(topo_map.get_possible_top_points(trail_head)) for trail_head in trail_heads]))


if __name__ == '__main__':
    main()
