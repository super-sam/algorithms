from dataclasses import dataclass
from functools import total_ordering
import heapq
import math
from typing import Dict, Union

@dataclass
@total_ordering
class WeightedVertex:
    weight: float
    neighbour: str
    vertex: str

    def __eq__(self, other: object) -> bool:
        return self.weight == other.weight
    def __lt__(self, other: object) -> bool:
        return self.weight == other.weight

def make_link(graph, node1, node2, weight):
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    graph[node1][node2] = {"weight": weight}
    graph[node2][node1] = {"weight": weight}


def find_smallest_path_from(vertex: str, in_graph: Dict[str, Dict[str, Dict[str, Union[int, bool]]]]) -> Dict[str, int]:
    neighbours = []
    path_map = {node: {"w": math.inf, "p": []} for node in in_graph}
    path_map[vertex]["w"] = 0

    for neighbour in in_graph[vertex]:
        weight = in_graph[vertex][neighbour]["weight"]
        in_graph[vertex][neighbour]["visited"] = True
        heapq.heappush(neighbours, (weight, neighbour, vertex))

    while neighbours:
        weight, to_vertex, from_vertex = heapq.heappop(neighbours)
        if path_map[to_vertex]["w"] > weight + path_map[from_vertex]["w"]:
            path_map[to_vertex]["w"] = weight + path_map[from_vertex]["w"]
            path_map[to_vertex]["p"] = path_map[from_vertex]["p"] + [from_vertex]

        for neighbour in in_graph[to_vertex]:
            if not in_graph[to_vertex][neighbour].get("visited"):
                weight = in_graph[to_vertex][neighbour]["weight"]
                in_graph[to_vertex][neighbour]["visited"] = True
                heapq.heappush(neighbours, (weight, neighbour, to_vertex))

    return path_map


if __name__ == "__main__":
    import sys
    import copy
    graph = {}
    fn = lambda x: int(x) if x.isdigit() else x
    for line in sys.stdin:
        node1, node2, weight = list(map(fn, line.split()))
        make_link(graph, node1, node2, weight)

    for key in graph:
        weight_map = find_smallest_path_from(key, copy.deepcopy(graph))
        print(key, weight_map)
