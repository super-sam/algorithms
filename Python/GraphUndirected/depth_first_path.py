from typing import List, Iterable
from dataclasses import dataclass
from graph import Graph


class DepthFirstPaths:
    def __init__(self, graph: Graph, source: int):
        self.__marked: List[bool] = []
        self.__edge_to: List[int] = []
        self.__source = source
        self.dfs(graph, source)

    def dfs(self, graph: Graph, node: int) -> None:
        self.__marked[node] = True
        for vertex in graph.adj(node):
            if not self.__marked[vertex]:
                self.dfs(graph, vertex)
                self.__edge_to[vertex] = node

    def has_path_to(self, vertex: int) -> bool:
        return self.__marked[vertex]

    def path_to(self, vertex: int) -> Iterable[int]:
        if not self.has_path_to(vertex):
            return None
        path: List[int] = []
        current = vertex
        while current != self.__source:
            path.append(current)
            current = self.__edge_to[current]
        path.append(current)
        return iter(path)

