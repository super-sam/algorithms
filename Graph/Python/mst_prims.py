from grapg import Graph, Vertex, Edge


from typing import List, Set, Tuple

def mst_prim(g: Graph, vertex: str) -> List[Edge]:
    result: List[Edge] = []
    visited: Set[str] = set()
    edges: List[Tuple[int, Edge]] = []
    
    def visit(vertex: str) -> None:
        visited.add(vertex)
        for edge in g.graph[vertex].edges:
            if edge.to_vertex in visited:
                continue
            heapq.heappush(edges, (edge.weight, edge))
    
    for edge in g.graph[vertex].edges:
        heapq.heappush(edges, (edge.weight, edge))

    while edges and len(result) < len(g.graph) - 1:
        _, edge = heapq.heappop(edges)
        
        if edge.to_vertex.name in visited and edge.from_vertex.name in visited:
            continue
        result.append(edge)
        if edge.to_vertex.name not in visited:
            visit(edge.to_vertex.name)
        if edge.from_vertex.name not in visited:
            visit(edge.from_vertex.name)
        
    return result



if __name__ == "__main__":
    graph = Graph()
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    g.add_edge(a, b, 2)
    g.add_edge(a, c, 3)
    g.add_edge(b, c, 1)
    g.add_edge(b, d, 1)
    g.add_edge(c, e, 1)
    g.add_edge(d, e, 2)
    g.add_edge(d, f, 3)
    g.add_edge(e, f, 1)
    g.add_edge(e, g, 2)
    g.add_edge(f, g, 1)
    mst = mst_prim(graph, 'A')
    for edge in mst:
        print(edge)