from collections import deque
import heapq
from typing import Iterable, List
from MinimunSpanningTree import edge_weighted_graph, edge
from UnionFind import weighted_union_find_path_compression

class KruskalMST:
    def __init__(self, edge_weighted_graph: edge_weighted_graph.EdgeWeightedGraph) -> None:
        self.__mst: Iterable[edge.Edge] = deque()
        pq: List[edge.Edge] = []
        for edge_item in edge_weighted_graph:
            pq.append(edge_item)
        
        uf: weighted_union_find_path_compression.WeightedUnionFindPC = weighted_union_find_path_compression.WeightedUnionFindPC(edge_weighted_graph.vertex_count())
        while pq and len(self.__mst) < edge_weighted_graph.vertex_count() - 1:
            edg: edge.Edge = heapq.heappop(pq)
            v = edg.either()
            w = edg.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self.__mst.append(edg)
    def edges(self):
        return iter(self.__mst)