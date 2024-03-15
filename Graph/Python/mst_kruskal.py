import heapq


from typing import List


class UnionFind:
    def __init__(self, vertices: List[str]):
        self.parent: Dict[str, str] = {vertex: vertex for vertex in vertices}
        self.size: Dict[str, int] = {vertex: 1 for vertex in vertices}
    
    def __root(self, vertex: str):
        while vertex != self.parent[vertex]:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex
    
    def is_connected(self, vertex1: str, vertex2: str) -> bool:
        return self.__root(vertex1) == self.__root(vertex2)
    
    def union(self, vertex1: str, vertex2: str) -> None:
        root1: str = self.__root(vertex1)
        root2: str = self.__root(vertex2)

        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] = self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] = self.size[root2]

def mst_kruskal(g: Graph) -> List[Edge]:
    edges = []
    visited = set()
    for vertex in g.graph:
        for edge in g.graph[vertex].edges:
            if str(edge) not in visited:
                heapq.heappush(edges, (edge.weight, str(edge), edge))
    
    result = []
    uf = UnionFind(vertices=[vertex for vertex in g.graph])
    while edges and len(result) < len(g.graph) - 1:
        weight, name, edge = heapq.heappop(edges)
        if uf.is_connected(edge.from_vertex.name, edge.to_vertex.name):
            continue
        uf.union(edge.from_vertex.name, edge.to_vertex.name)
        result.append(edge)
    
    return result

if __name__ == "__main__":
    g = Graph()
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
    mst = g.mst_kruskal()
    for edge in mst:
        print(edge)