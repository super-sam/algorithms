from graph import Graph, Vertex


from typing import List, Optional


def topological_sort(dag) -> Optional[List[Vertex]]:
    visited = set()
    visiting = set()
    result = []
    def topological_sort_util(vertex: Vertex) -> bool:
        visited.add(vertex.name)
        visiting.add(vertex.name)
        for neighbour in dag.vertices(vertex):
            if neighbour.name in visiting:
                return False
            if neighbour.name in visited:
                continue
            if topological_sort_util(neighbour):
                return False
        visiting.remove(vertex.name)
        result.append(vertex)
        return True

    for vertex_name in dag.graph:
        if vertex_name in visited:
            continue
        if not topological_sort_util(dag.graph[vertex_name]):
            return None
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
    print(topological_sort(graph))  # False
    graph.add_edge(d, a)
    print(topological_sort(graph))  # True