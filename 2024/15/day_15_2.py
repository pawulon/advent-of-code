from pathlib import Path

from day_15_1 import read_map_and_moves, Warehouse, Map


def scale_warehouse(warehouse: Map) -> Map:
    new_warehouse = []
    for line in warehouse:
        current_line = []
        for element in line:
            if element == "#":
                current_line += ["#", "#"]
            elif element == "O":
                current_line += ["[", "]"]
            elif element == ".":
                current_line += [".", "."]
            elif element == "@":
                current_line += ["@", "."]
        new_warehouse.append(current_line)
    return new_warehouse


def main():
    warehouse_map, moves = read_map_and_moves(Path("input.txt"))
    warehouse_map = scale_warehouse(warehouse_map)
    warehouse = Warehouse(warehouse_map, moves)
    warehouse.move_robot()
    print(warehouse.get_sum_of_boxes_gps(big_box=True))


if __name__ == '__main__':
    main()
