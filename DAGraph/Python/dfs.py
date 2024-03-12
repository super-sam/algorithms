from graph import Graph, Vertex
from collection import deque

from typing import List

def bfs(graph: Graph, vertex: Vertex) -> List[Vertex]:
    queue = deque()
    visited = set()
    result = []
    queue.append(vertex)
    visited.add(vertex.name)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph.vertices(vertex):
            if neighbour.name in visited:
                continue
            queue.append(neighbour)

    return result


if __name__ == "__main__":
    graph = Graph()
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    print(graph.bfs(a))  # [A, B, C, D]