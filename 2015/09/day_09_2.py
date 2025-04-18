from pathlib import Path

from day_09_1 import read_distances, remove_city, Distances


def find_longest_path(graph: Distances) -> int:
    lengths = []
    for city in graph.keys():
        lengths.append(find_longest_path_with_starting_point(city, graph))
    return max(lengths)


def find_longest_path_with_starting_point(start: str, graph: Distances) -> int:
    if len(graph) == 1:
        return 0
    lengths = []
    graph_without_start = remove_city(graph, start)
    for target in graph[start].keys():
        lengths.append(graph[start][target] + find_longest_path_with_starting_point(target, graph_without_start))
    return max(lengths)


def main():
    distances = read_distances(Path('input.txt'))
    maximal_path = find_longest_path(distances)
    print(maximal_path)


if __name__ == '__main__':
    main()
