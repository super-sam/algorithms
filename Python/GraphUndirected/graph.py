from __future__ import annotations
import sys
from collections import defaultdict
from typing import Iterable, Final


class Graph:
    def __init__(self, v: int):
        self.v: Final = v
        self.g = defaultdict(list)

    @classmethod
    def from_input_stream(cls, stream: sys.stdin):
        count = 0
        cls.g = defaultdict(list)
        for line in stream:
            v, w = line.split(" ")
            cls.add_edge(v, w)
            count += 1
        cls.v = count

    def add_edge(self, v: int, w: int) -> None:
        self.g[v].append(w)
        self.g[w].append(v)

    def adj(self, v: int) -> Iterable[int]:
        return iter(self.g[v])

    def vertices_count(self) -> int:
        return self.v

    def edges_count(self) -> int:
        edges = 0
        for vertex in self.g:
             edges += self.degree(self.g, vertex)

        return edges // 2

    def __str__(self) -> str:
        pass

    @staticmethod
    def degree(graph: Graph, vertex: int) -> int:
        degree: int = 0
        for _ in graph.adj(vertex):
            degree += 1
        return degree

    @staticmethod
    def max_degree(graph: Graph) -> int:
        int max_deg = 0
        for v in range(graph.vertices_count()):
            if Graph.degree(graph, v) > max_deg:
                max_deg = Graph.degree(graph, v)
        return max_deg

    @staticmethod
    def avg_degree(graph: Graph) -> float:
        return 2.0 * graph.edges_count() / graph.vertices_count()


    @staticmethod
    def self_loop_count(graph: Graph) -> int:
        count: int = 0
        for v in range(graph.vertices_count()):
            for w in graph.adj(v):
                if v == w:
                    count += 1
        return count // 2


if __name__ == '__main__':
    my_graph = Graph.from_input_stream(sys.stdin)
    for vertex in range(my_graph.vertices_count()):
        for w in range(my_graph.adj(vertex)):
            print(f"{vertex} - {w}")




