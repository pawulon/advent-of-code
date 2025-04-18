from pathlib import Path

Distances = dict[str, dict[str, int]]


def read_distances(input_path: Path) -> Distances:
    distances = {}
    for line in input_path.read_text().splitlines():
        start, _, end, _, distance = line.split()
        distances.setdefault(start, {})
        distances.setdefault(end, {})
        distances[start][end] = int(distance)
        distances[end][start] = int(distance)
    return distances


def remove_city(graph: Distances, city_to_delete: str) -> Distances:
    return {
        city: {dest: dist for dest, dist in targets.items() if dest != city_to_delete}
        for city, targets in graph.items() if city != city_to_delete
    }

def find_shortest_path(graph: Distances) -> int:
    lengths = []
    for city in graph.keys():
        lengths.append(find_shortest_path_with_starting_point(city, graph))
    return min(lengths)

def find_shortest_path_with_starting_point(start: str, graph: Distances) -> int:
    if len(graph) == 1:
        return 0
    lengths = []
    graph_without_start = remove_city(graph, start)
    for target in graph[start].keys():
        lengths.append(graph[start][target] + find_shortest_path_with_starting_point(target, graph_without_start))
    return min(lengths)

def main():
    distances = read_distances(Path('input.txt'))
    minimal_path = find_shortest_path(distances)
    print(minimal_path)


if __name__ == '__main__':
    main()
