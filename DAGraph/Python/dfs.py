from graph import Graph, Vertex


from typing import List


def dfs_iterative(graph, vertex: Vertex) -> List[Vertex]:
    result = []
    visited = set()
    stack = []
    stack.append(vertex)
    visited.add(vertex.name)
    while stack:
        vertex = stack.pop()
        result.append(vertex)
        for neighbour in graph.vertices(vertex)[::-1]:
            if neighbour.name in visited:
                continue
            stack.append(neighbour)
            visited.append(neighbour.name)

    return result

def dfs(graph, vertex: Vertex) -> List[Vertex]:
    result = []
    visited = set()

    def dfs_util(vertex: Vertex) -> None:
        visited.add(vertex.name)
        result.append(vertex)
        for neighbour in graph.vertices(vertex):
            if neighbour.name in visited:
                continue
            dfs_util(neighbour) 

    dfs_util(vertex)

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
    print(dfs(graph, a))  # [A, B, C, D] 