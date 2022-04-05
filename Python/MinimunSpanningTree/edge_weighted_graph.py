import sys
from collections import defaultdict
from typing import Iterable
import edge


class EdgeWeightedGraph:
    def __init__(self, vertices: int):
        self.__vertices = vertices
        self.__items = defaultdict(list)

    @classmethod
    def from_input_stream(cls, stream: sys.stdin):
        count = 0
        cls.g = defaultdict(list)
        for line in stream:
            v, w, weight = list(map(lambda x: int(x) if x.isdigit() else x, line.split()))
            edg: edge.Edge = edge.Edge(v, w, weight)
            cls.add_edge(edg)
            count += 1
        cls.v = count

    def add_edge(self, graph_edge: edge.Edge):
        """Add a weighted edge to this graph"""
        vertex: int = graph_edge.either()
        other_vertex: int = graph_edge.other(vertex)
        self.__items[vertex].append(graph_edge)
        self.__items[other_vertex].append(graph_edge)

    def adj(self, vertex: int) -> Iterable[edge.Edge]:
        """Edge incident to vertex"""
        return iter(self.__items[vertex])

    def edges(self) -> Iterable[edge.Edge]:
        """All the edges in the graph"""
        pass

    def vertex_count(self) -> int:
        """Number of vertices"""
        pass

    def edge_count(self) -> int:
        """Number of edges"""
        pass

    def __str__(self) -> str:
        """string representation"""
        pass
