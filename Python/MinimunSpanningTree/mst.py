import sys
from typing import Iterable
import edge_weighted_graph
import edge

class MST:
    def __init__(self, graph: edge_weighted_graph.EdgeWeightedGraph) -> None:
        pass

    def edges(self) -> Iterable[edge.Edge]:
        pass

    def weight() -> float:
        pass

if __name__ == "__main__":
    graph: edge_weighted_graph.EdgeWeightedGraph = edge_weighted_graph.EdgeWeightedGraph.from_input_stream(sys.stdin)
    mst: MST = MST(graph)
    for edg in mst.edges():
        print(edg)
    print(f"{mst.weight():.2f}")
