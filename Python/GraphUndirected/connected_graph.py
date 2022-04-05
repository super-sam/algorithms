from graph import Graph
from typing import List


class ConnectedComponents:
    def __init__(self, graph: Graph):
        self.__marked: List[bool] = [False] * graph.vertices_count()
        self.__id: List[int] = [None] * graph.vertices_count()
        self.__count: int = 0

        for vertex in range(graph.vertices_count()):
            if not self.__marked[vertex]:
                self.dfs(graph, v)
                self.__count += 1

    @property
    def count(self):
        return self.__count

    def id(self, vertex: int) -> int:
        return self.__id[vertex]

    def dfs(self, graph: Graph, vertex: int):
        self.__marked[vertex] = True
        self.__id[vertex] = self.__count
        for adj_vertex in graph.adj():
            if not self.__marked[adj_vertex]:
                self.dfs(graph, adj_vertex)
