from typing import Iterable
from Tree import diedge

class EdgeWeightedDiGraph:
    def __init__(self, vertices: int) -> None:
        self.__vertices = vertices
        self.__edges = [[] for vertex in range(vertices)]

    def add_edge(self, edge: diedge.DiEdge) -> None:
        v: int = edge.from_edge()
        self.__edges[v].append(edge)

    def adj(self, vertex: int) -> Iterable[diedge.DiEdge]:
        return iter(self.__edges[vertex])

    def vertex_count(self) -> int:
        pass

    def edge_count(self) -> int:
        pass

    def edges(self) -> Iterable[diedge.DiEdge]:
        pass
    
    def __str__(self) -> str:
        pass
