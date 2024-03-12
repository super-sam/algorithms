class Vertex:
    def __init__(self, name: str)-> None:
        self.name = name
        self.edges = []
    
    def __repr__(self) -> str:
        return  f"Vertex({self.name})"
    
    def __str__(self) -> str:
        return self.name

class Edge:
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, weight: int) -> None:
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"Edge({self.from_vertex}, {self.to_vertex}, {self.weight})"
    
class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex: Vertex) -> None:
        self.graph[vertex.name] = vertex
    
    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int = 0) -> None:
        if from_vertex.name not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex.name not in self.graph:
            self.add_vertex(to_vertex)
        edge = Edge(from_vertex, to_vertex, weight)
        from_vertex.add_edge(edge)

    def edges(self, vertex: Vertex) -> List[Edge]:
        if vertex.name not in self.graph:
            raise KeyError
        return self.graph[vertex.name].edges
    
    def vertices(self, vertex: Vertex) -> List[Vertex]:
        if vertex.name not in self.graph:
            raise KeyError
        return [edge.to_vertex for edge in self.edges(vertex)]