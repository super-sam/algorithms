class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []
    
    def __repr__(self):
        return f"Vertex({self.name})"
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, weight: int):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    def __repr__(self):
        return f"Edge({self.from_vertex.name}, {self.to_vertex.name}, {self.weight})"

    def __str__(self):
        name = "-".join(sorted([self.from_vertex.name, self.to_vertex.name]))
        return f"{name}-{self.weight}"
    
    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        if str(self) < str(other):
            return True
        return False


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex: Vertex) -> None:
        self.graph[vertex.name] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int = 0) -> None:
        for vertex in [from_vertex, to_vertex]:
            if vertex.name not in self.graph:
                self.add_vertex(vertex)
        
        from_vertex.edges.append(Edge(from_vertex, to_vertex, weight))
        to_vertex.edges.append(Edge(to_vertex, from_vertex, weight))

