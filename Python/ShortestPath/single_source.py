from typing import Iterable
from MinimunSpanningTree import edge_weighted_digraph.edge_weighted_digraph.EdgeWeightedDiGraph
from MinimunSpanningTree import diedge.DiEdge
from typing import List


class SingleSource:
    def __init__(self, graph: edge_weighted_digraph.EdgeWeightedDiGraph) -> None:
        self.edge_to = []
        self.dist_to = []
    
    def dist_to(self, vertex: int) -> int:
        return self.dist_to[vertex]

    def path_to(self, vertex: int) -> Iterable[diedge.DiEdge]:
        path: List[diedge.DiEdge] = []
        for e in self.edge_to[vertex]:
            path.append(e)
        return iter(path)

    def has_path_to(self, vertex: int) -> bool:
        pass

if __name__ == "__main__":
    graph = edge_weighted_digraph.edge_weighted_digraph.EdgeWeightedDiGraph(8)
    source = 0
    shortest_path: SingleSource = SingleSource(graph, source)

    for v in graph.vertex_count():
        print(f"{source} to {v}: {shortest_path.dist_to(v):.2f}", end=" ")
        for edge in shortest_path.path_to(v):
            print(edge, end=" ")
        print()
    
        
        