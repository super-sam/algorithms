from graph import Graph, Vertex

def has_cycle(dag: Graph) -> bool:
    visited = set()
    visiting = set()
    def has_cycle_util(vertex: Vertex) -> bool:
        visited.add(vertex.name)
        visiting.add(vertex.name)
        for neighbour in dag.vertices(vertex):
            if neighbour.name in visiting:
                return True
            if neighbour.name in visited:
                continue
            if has_cycle_util(neighbour):
                return True
        visiting.remove(vertex.name)
        return False
    
    for vertex_name in dag.graph:
        if vertex_name in visited:
            continue
        if has_cycle_util(dag.graph[vertex_name]):
            return True
    return False


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
    print(has_cycle(graph))  # False
    graph.add_edge(d, a)
    print(has_cycle(graph))  # True