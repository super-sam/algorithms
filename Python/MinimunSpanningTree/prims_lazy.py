import heapq
from collections import deque
from typing import Deque, Iterable, List
from MinimunSpanningTree import edge, edge_weighted_graph

class PrimLazy:
    def __init__(self, graph: edge_weighted_graph.EdgeWeightedGraph) -> None:
        self.__mst: Deque[edge.Edge] = deque()
        self.__pq: List[edge.Edge] = []
        self.__marked: List[bool] = [False] * graph.vertex_count()
        self.visit(graph, 0)

        while self.__pq:
            e: edge.Edge = heapq.heappop(self.__pq)
            v: int = e.either()
            w: int = e.other(v)
            if self.__marked[v] and self.__marked[w]:
                continue
            self.__mst.append(edge)
            if not self.__marked[v]:
                self.visit(graph, v)
            if not self.__marked[w]:
                self.visit(graph, w)
    
    def visit(self, graph: edge_weighted_graph.EdgeWeightedGraph, vertex: int):
        self.__marked[vertex] = True
        for e in graph.adj(vertex):
            if not self.__marked[e.other(vertex)]:
                self.__pq.append(e)
    
    def mst(self) -> Iterable[edge.Edge]:
        return iter(self.__mst)
